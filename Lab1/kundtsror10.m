function Amax = kundtsror10(L,v,f,kappa,r,plots)
% Inputparametre: 
% L: r?rets lengde (m), v: lydhastighet i luft (m/s), f: frekvens (Hz),
% kappa: refleksjonskoeffisient (f.eks. 0.95), r: antall refleksjoner (-).
% Programmet er opprinnelig skrevet av Arnt Inge Vistnes september 2012.

xmax = L*r;         % Lydveiens lengde (inkl. refleksjoner)
lambda = v/f;       % Beregnet b?lgelengde
dx = lambda/128.0;  % Oppl?sning i beregningene, gitt per bolgelengde
N = floor(L/dx);    % Beregningsarrayens lengde
R = floor(r);       % Antall refleksjoner innen den gitte tiden siden start
t = xmax/v;         % Tiden siden start
totKappa = kappa^(floor(r));  % Amplitude etter alle refleksjonene
fprintf('Lyden g?r %6.2f r?rlengder p? tiden %5.4f s.\n', r, t);
fprintf('Lydintensiteten er da %9.4g x opprinnelig verdi.\n\n',totKappa);
if (totKappa>0.001)
    rmin = 1 + floor(log(0.001)/log(kappa));
    fprintf(2,'********************************************************************\n')
    fprintf(2,'* Du m? ?ke antall refleksjoner til minst %4d                     *\n',rmin)
    fprintf(2,'* slik at amplityden etter alle refleksjoner er mindre enn 0.001.  *\n')
    fprintf(2,'* Hvis ikke, representerer ikke resultatene den stasjon?re         *\n')
    fprintf(2,'* tilstanden som vi m?ler i laboratoriet.                          *\n')
    fprintf(2,'********************************************************************\n')
    Amax = -999;
    return;
end;
k = 2.0*pi/lambda;  % B?lgetallet
TN = 33;            % Antall plot i l?pet av en periode 
x = linspace(0,L,N);% X-akse i plot (posisjon langs Kunds r?r)
A = zeros(N,1);     % Array for ? lagre amplitudene
Amax = zeros(N,1);  % Lagrer max i hvert pkt for ulike tider

%*************************************************************************
if (plots)
    fprintf('F?rste plot:\n');
end;
fprintf('B?lgen ved ulike tidpunkt fordelt over en periode\n');

for tt = 1:TN                       % Ytre l?kke: TN tider innen en periode 
    A = zeros(N,1);                 % Array for ? lagre amplitudene
    faseT = 2.0*pi*(tt-1)/(TN-1);   % Faseledd som skyldes tid
    for i=1:N                           % Gjennoml?per alle posisjoner i r?ret   
        for j = 0:R                     % Bidrag fra alle refleksjoner
            xsign = (-1)^j;
            Lkorr = 2.0*L*floor((j+1)/2);
            if (floor((j+1)/2) == floor(j/2))
                xtot = j*L + i*dx;      % Framover i r?ret
            else
                xtot = j*L + (N-i)*dx;  % Bakover i r?ret
            end;
            if (xtot<xmax)              % Tar bare med b?lgen inntil gitt tid
                A(i) = A(i) + (kappa^j)*cos(k*(Lkorr + xsign*i*dx)-faseT);
            end;
        end;    
    end;
    if (plots)
        plot(x,A,'-r');                 % Plotter bolgen for hver fase i tid
        xlabel('Posisjon langs r?ret (m)');
        ylabel('Rel. amplitude');
        title('B?lgen ved ulike tider innen en periode');
        hold on;
    end;
    for m = 1:N             % Lagrer h?yeste verdi for ulike t
        if (A(m)>Amax(m)) 
            Amax(m) = A(m);
        end;
    end;
end;

% Beregner max amplitude overhodet, max amplitude i slutten av r?ret,
% samt Amplitude Standing Wave Ratio (ASWR):
fprintf('   Max amplitude: %6.2f \n',max(Amax));
%fprintf('   Max amplitude ved mikrofonens plass: %6.2f \n',Amax(N));
ASWR = max(Amax)/min(Amax);
fprintf('   Amplitude standing wave ratio (ASWR): %5.3f \n',ASWR);
fprintf('   Theoretical standing wave ratio     : %5.3f \n\n',(1+kappa)/(1-kappa));

% %*************************************************************************
if (plots) 
    fprintf('Andre plot:\n');
    fprintf('Animering f?lger b?lgen i tid 1 periode\n\n');

    figure;
    p = plot(x,A,'-','EraseMode','xor');    % Klargjoring til animering
    yaxis = 1.2*max(Amax);
    axis([0 L -yaxis yaxis])
    xlabel('Posisjon langs r?ret (m)');
    ylabel('Rel. amplitude');
    title('Animering av b?lgen, en periode');
    hold on
    for tt = 1:TN                       % Ytre l?kke: TN tider innen en periode
        A = zeros(N,1);                 % Array for ? lagre amplitudene
        faseT = 2.0*pi*(tt-1)/(TN-1);   % Faseledd som skyldes tid
        for i=1:N                           % Gjennoml?per alle posisjoner i r?ret   
            for j = 0:R                     % Bidrag fra alle refleksjoner
                xsign = (-1)^j;
                Lkorr = 2.0*L*floor((j+1)/2);
                if (floor((j+1)/2) == floor(j/2))
                    xtot = j*L + i*dx;      % Framover i r?ret
                else
                    xtot = j*L + (N-i)*dx;  % Bakover i r?ret
                end;
                if (xtot<xmax)
                    A(i) = A(i) + (kappa^j)*cos(k*(Lkorr + xsign*i*dx)-faseT);
                end;
            end;    
        end;
        set(p,'XData',x,'YData',A) 
        drawnow
        pause(0.10);  % Forsinker fremvisningen av b?lgen (juster for din pc)
    end;
end;
% %*************************************************************************
% 
    



