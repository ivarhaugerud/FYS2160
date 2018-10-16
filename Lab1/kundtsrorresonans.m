% Dine eksperimentelle data
% f er frekvensen du m?lte ved
f = [650 660 669.5 675 680 682 684 686 688 690.5 692.5 694.5 696 697.5 699 699.5 700 701 702 703 704 705 706.5 708 710 715 720 730];
% Hvis du har m?lt en litt annen lengde p? r?ret og/eller en litt annen
% lydhastighet enn det som er brukt i programmet, vil toppen av
% resonanskurven dukke opp p? en litt annen frekvens enn du fant. Da bare
% forskyver vi kurven litt
f = f-5; 
% p er amplituden du m?lte med multimeteret
p = [41 47 58 68 81 93 101 113 134 163 209 283 330 486 614 614 603 560 480 380 320 286 212 179 149 103 79 54];

p2 = (p/max(p)).^2; % Intensitet

% Simuleringsprogramting
kappa = [0.85 0.97]; % kappa, legg gjerne til flere, eks [0.90 0.95]
resonansfrekvens = 696; % Din favorittresonansfrekvens [Hz]
v = 343.2; % Lydhastigheten [m/s]
L = 1.24; % Lengden p? r?ret [m]
r = 100; % Antall refleksjoner

fprintf(2,'*----------------------------------------------------------------------------------*\n')
fprintf(2,'| Du m? editere resultatene og parametrene over. Det du kj?rer n? er et eksempel...|\n')
fprintf(2,'| Samtidig b?r du kommentere disse fprintf-linjene. :-)                            |\n')
fprintf(2,'*----------------------------------------------------------------------------------*\n')

% Frekvensene du vil l?pe over, fra:steg:til. Endre gjerne rekkevidden.
frekvenser = resonansfrekvens-20:1:resonansfrekvens+20; 

Amax = zeros(length(frekvenser),length(kappa)); % Max amplitude for en gitt frekvens
Amax_rel = zeros(length(frekvenser),length(kappa));
Imax_rel = zeros(length(frekvenser),length(kappa));

for i = 1:length(kappa) % L?per over kappaene
    fprintf('kappa is %1.2f\n',kappa(i))
    for j = 1:length(frekvenser) % L?per over frekvensene
        % Endre hvis du bruker en annen versjone enn 10
        Amax_tmp = kundtsror10(L,v,frekvenser(j),kappa(i),r,false);
        if (length(Amax_tmp) == 1)
            return
        end;
        Amax(j,i) = max(Amax_tmp);
    end
    % Finner relative amplituder og intensiteter
    for j = 1:length(frekvenser)
        Amax_rel(j,i) = Amax(j,i)/max(Amax(:,i));
        Imax_rel(j,i) = Amax_rel(j,i).^2;
    end
end

% Plottedel
markerType = char('-bo','-rx','-g*','--bo','--rx','--g*');
l = cell(1,length(kappa)+1);
for i = 1:length(kappa)
    plot(frekvenser,Amax_rel(:,i),markerType(i,:));
    xlabel('Frekvens [Hz]');
    ylabel('Relativ amplitude');
    hold on;
    l{i} = num2str(kappa(i));
end
l{length(l)} = 'data';
plot(f,p/max(p),'.-k');
legend(l);

figure;
for i = 1:length(kappa)
    plot(frekvenser,Imax_rel(:,i),markerType(i,:));
    xlabel('Frekvens [Hz]');
    ylabel('Relativ intensitet');
    hold on;
end
plot(f,p2,'.-k');
legend(l);

fprintf(2,'*----------------------------------------------------------------------------------*\n')
fprintf(2,'| Du m? editere resultatene og parametrene i begynnelsen av programmet.            |\n') 
fprintf(2,'| Det du kj?rer n? er et eksempel. Samtidig b?r du kommentere begge sett med       |\n')
fprintf(2,'| fprintf-linjene. :-)                                                             |\n')
fprintf(2,'*----------------------------------------------------------------------------------*\n')
