import streamlit as st
import numpy as np

class R: pass
class F: pass

# KDS - 2021 (RC : Reinforced Concrete) - Doubly (Singly 포함)
def RC(In):
	# Input Data
    be = In.be; 	        height = In.height
    fck = In.fck;			fy = In.fy;			Es = In.Es
    depth = In.depth;		As = In.As;			dt = In.dt
    depth1 = In.depth1;		As1 = In.As1
	# Input Data

    ep_y = fy/Es;  ep_smin = 0.004
    if fy >= 400:  ep_smin = 2*ep_y
    
    # 계수 (Coefficient)
    n = 2;  ep_co = 0.002;  ep_cu = 0.0033
    
    if fck > 40:
        n = 1.2 + 1.5*((100 - fck)/60)**4
        ep_co = 0.002 + (fck - 40)/1e5
        ep_cu = 0.0033 - (fck - 40)/1e5
    
    if n >= 2:  n = 2
    n = round(n*100)/100
    
    alpha = 1 - 1/(1 + n)*(ep_co/ep_cu);  temp = 1/(1 + n)/(2 + n)*(ep_co/ep_cu)**2
    if fck <= 40:  alpha = 0.8
    beta = 1 - (0.5 - temp)/alpha
    if fck <= 50:  beta = 0.4
    alpha = round(alpha*100)/100;  beta = round(beta*100)/100;  beta1 = 2*beta;    
    eta = alpha/beta1;  eta = round(eta*100)/100
    if fck == 50:  eta = 0.97
    if fck == 80:  eta = 0.87
	# 계수 (Coefficient)

	# % 철근비 (rho)
    rho_s = As/(be*depth);  rho_s1 = As1/(be*depth)
    rho_sb = beta1*eta*(0.85*fck)/fy * ep_cu/(ep_cu + ep_y)
    rho_smax = beta1*eta*(0.85*fck)/fy * ep_cu/(ep_cu + ep_smin) *dt/depth
	# % 철근비 (rho)

    # % 중립축 위치(c or a) 및 설계강도 (phi*Mn)
    rho_comY = beta1*eta*(0.85*fck)/fy * (depth1/depth) * ep_cu/(ep_cu - ep_y) + rho_s1
    if rho_s >= rho_comY:				# 압축철근 항복 (압축철근이 항복하기 위한 최소 철근비)
        a = (As - As1)*fy/(eta*0.85*fck*be);  c = a/beta1;  Com_Rein_Status = 'Yielding'
    else:								# 압축철근 항복하지 않음
        p = eta*(0.85*fck)*be*beta1;  q = (As1*Es*ep_cu - As*fy);  r = -As1*Es*ep_cu*depth1
        c = (-q + np.sqrt(q**2 - 4*p*r))/(2*p);  a = beta1*c;  Com_Rein_Status = 'Not  Yielding'
	
    ep_s1 = ep_cu*(c - depth1)/c;  f_s1 = Es*ep_s1;  ep_t = ep_cu*(dt - c)/c
    ep_s = ep_cu*(depth - c)/c;	   f_s = Es*ep_s
    if f_s >= fy:   f_s = fy
    if f_s1 >= fy:  f_s1 = fy
		
	# % 강도감소계수 (phi) : 띠철근 기준
    ep_tccl = ep_y;  ep_ttcl = 0.005
    if fy >= 400:  ep_ttcl = 2.5*ep_y
    phi = 0.65 + (ep_t - ep_tccl)*(0.85 - 0.65)/(ep_ttcl - ep_tccl);  phi_Status = 'Transition  Zone'
    if ep_t <= ep_tccl:  phi = 0.65;  phi_Status = 'Compression  Controlled'
    if ep_t >= ep_ttcl:  phi = 0.85;  phi_Status = 'Tension  Controlled'
    Failure_Mode = '✅  Steel  Yielding'
    if ep_t < ep_smin:  Failure_Mode = '❌  NG  (Concrete  Crushing)'
	# % 강도감소계수 (phi) : 띠철근 기준
		
    Cs = As1*f_s1/1e3;	Cc = eta*(0.85*fck)*a*be/1e3
    Ts = Cs;			Tc = (As*fy - As1*f_s1)/1e3
    Mn = Ts*(depth - depth1)/1e3 + Tc*(depth - a/2)/1e3;  Md = phi*Mn
	# % 중립축 위치(c or a) 및 설계강도 (phi*Mn)

    # % 철근비 체크
    lamda = 1;  fr = 0.63*lamda*np.sqrt(fck);  Ig = be*height**3/12;  yt = height/2
    Mcr = (fr*Ig)/yt/1e6
    rho_smin = 1.2*Mcr*1e6/(phi*fy*(depth - a/2))/(be*depth);  rho_Check = '✅  Under-Reinforced'
    rho_sbD = rho_sb + rho_s1*(f_s1/fy)
    rho_smaxD = rho_smax + rho_s1*(f_s1/fy)
    if rho_s < rho_smin:  rho_Check = '❌  NG  (<i>ρ</i>  <  <i>ρ<sub>min</sub></i>)'
    if rho_s > rho_smaxD: rho_Check = '❌  NG  (Over-Reinforced)'
	# % 철근비 체크

    if 'Singl' in In.Type:  ep_s1 = '-';  Com_Rein_Status = '-';  Ts = 0

    R.eta = eta
    R.beta1 = beta1;		R.ep_cu = ep_cu;			R.ep_y = ep_y;			R.fy = fy;		R.ep_c = ep_cu
    R.ep_s = ep_s;			R.f_s = f_s;				R.Failure_Mode = Failure_Mode
    R.ep_s1 = ep_s1;		R.f_s1 = f_s1;				R.Com_Rein_Status = Com_Rein_Status;	R.ep_t = ep_t
    R.rho_smin = rho_smin;	R.rho_s = rho_s;			R.rho_sb = rho_sb;		R.rho_sbD = rho_sbD;  R.rho_comY = rho_comY
    R.rho_smax = rho_smax;	R.rho_smaxD = rho_smaxD;	R.rho_s1 = rho_s1;		R.rho_Check = rho_Check
    R.phi = phi;			R.phi_Status = phi_Status
    R.a = a;				R.c = c;					R.Cs = Cs;				R.Ts = Ts
    R.Cc = Cc;				R.Tc = Tc;					R.Mn = Mn;				R.Md = Md

    return R

# ACI 440. 1R -15 기반으로 설계식 제안 (FRP : FRP Concrete) - Doubly(Singly 포함)
def FRP(In):
	# % Input Data
    be = In.be; 	        height = In.height
    fck = In.fck;			f_fu = In.f_fu;			Ef = In.Ef
    depth = In.depth;		Af = In.Af;			    dt = In.dt
    depth1 = In.depth1;		Af1 = In.Af1
	# % Input Data

    ep_fu = f_fu/Ef

	# % 계수 (Coefficient)
    ep_cu = 0.003;  beta1 = 0.85
    if fck >= 28:  beta1 = 0.85 - 0.007*(fck - 28)
    if beta1 < 0.65:  beta1 = 0.65
	# % 계수 (Coefficient)

	# % 보강비 (rho)
    rho_f = Af/(be*depth);		rho_f1 = Af1/(be*depth)
    rho_fb = beta1*(0.85*fck)/f_fu*ep_cu/(ep_cu + ep_fu)
	# % 보강비 (rho)

    f_f1 = f_fu  # 압축 보강재 파괴된 것으로 초기에 가정
    for kk in range(3):  # 3번 반복        
        rho_fbD = rho_fb + rho_f1*f_f1/f_fu

        # % 강도감소계수 (phi)
        phi = 0.3 + 0.25*rho_f/rho_fbD;        phi_Status = 'Transition  Zone'
        if rho_f <= rho_fbD:      phi = 0.55;  phi_Status = 'Tension  Controlled'
        if rho_f >= 1.4*rho_fbD:  phi = 0.65;  phi_Status = 'Compression  Controlled'
        
        # % 중립축 위치(c or a) 및 설계강도 (phi*Mn)
        if rho_f >= rho_fbD:  # Over-reinforced : Concrete crushing
            Failure_Mode = '✅  Concrete  Crushing';  rho_Check = '✅  Over-Reinforced'
            p = (0.85*fck)*be*beta1;  q = (Af1 + Af)*Ef*ep_cu;  r = -(Af1*Ef*ep_cu*depth1 + Af*Ef*ep_cu*depth)
            c = (-q + np.sqrt(q**2 - 4*p*r))/(2*p);  a = beta1*c
        else:                 # Under-reinforced : FRP Rupture
            Failure_Mode = '✅  FRP  Rupture';  rho_Check = '✅  Under-Reinforced'
            cb = ep_cu*depth/(ep_cu + ep_fu);  c = cb;  a = beta1*c

            # %p = 0.85*fck*be*beta1;  q = (Af1*Ef*ep_cu - Af*f_fu);  r = -Af1*Ef*ep_cu*depth1;
            # %p = 0.85*fck*be*beta1;  q = -(Af*f_fu + Af1*Ef*ep_fu + 0.85*fck*be*beta1*depth);  r = (Af*f_fu*depth + Af1*Ef*ep_fu*depth1);
            # %c1 = (-q + sqrt(q**2 - 4*p*r))/(2*p);  a = beta1*c;
            # %c2 = (-q - sqrt(q** 2 - 4*p*r))/(2*p);  a = beta1*c;
        ep_f1 = ep_cu*(c - depth1)/c;	f_f1 = Ef*ep_f1;	ep_t = ep_cu*(dt - c)/c
        ep_f = ep_cu*(depth - c)/c;		f_f = Ef*ep_f
        if f_f >= f_fu:  f_f = f_fu

    Com_Rein_Status = 'Rupture'
    if f_f1 < f_fu:  Com_Rein_Status = 'Not  Rupture'
    rho_fmin = max(0.41*np.sqrt(fck)/f_fu, 2.3/f_fu)
    if rho_f < rho_fmin:  rho_Check = '❌  NG  (<i>ρ</i>  <  <i>ρ<sub>min</sub></i>)'
    Cf = Af1*f_f1/1e3;	Cc = (0.85*fck)*a*be/1e3
    Tf = Cf;			Tc = Af*f_f/1e3 - Tf
    Mn = Tf*(depth - depth1)/1e3 + Tc*(depth - a/2)/1e3;	Md = phi*Mn

    if 'Singl' in In.Type:  ep_f1 = '-';  Com_Rein_Status = '-';  Tf = 0

    F.beta1 = beta1;		F.ep_cu = ep_cu;		F.ep_fu = ep_fu;		F.f_fu = f_fu;		F.ep_c = ep_cu
    F.ep_f = ep_f;			F.f_f = f_f;			F.Failure_Mode = Failure_Mode
    F.ep_f1 = ep_f1;		F.f_f1 = f_f1;			F.Com_Rein_Status = Com_Rein_Status;			F.ep_t = ep_t
    F.rho_fmin = rho_fmin;	F.rho_f = rho_f;		F.rho_fb = rho_fb;		F.rho_fbD = rho_fbD
    F.rho_f1 = rho_f1;		F.rho_Check = rho_Check
    F.phi = phi;			F.phi_Status = phi_Status
    F.a = a;				F.c = c;				F.Cf = Cf;				F.Tf = Tf
    F.Cc = Cc;				F.Tc = Tc;				F.Mn = Mn;				F.Md = Md

    return F
