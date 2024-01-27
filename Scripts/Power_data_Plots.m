%1 for MiniPC
%2 for Raspberry Pi

scheme = ["secp256r1", "x25519","Kyber"];

plot = 1





%mWhTokWh = 0.000001
%c_energy = c_energy*mWhTokWh

width = 0.9;
distanceapart = 0.5
x = [1, 2, 3, 4 + distanceapart, 5 + distanceapart, 6 + distanceapart];

fig = figure;
left_color = [0, 0, 0]
right_color = [0, 0, 0]
set(fig,'defaultAxesColorOrder',[left_color; right_color]);

hold on;

if plot == 1
    % Data from Experimental Data/MiniPC_PWR_data.xlsx file
    time = [146.09,109.17,34.03]; % in us
    m_pwr = [19.79, 20.22,20.01] - 11.21; % in watt 11.21 is the avergae PWR without our script running
    c_energy =  time.*m_pwr/1000; %milliwatt-hour
    ylim([0, 10]);
elseif plot == 2
    % Data from Experimental Data/RPi_PWR_data.xlsx file
    time = [437.60,377.55,101.12]; % in us
    m_pwr = [5.85, 5.75,5.80] - 4.46; % in watt 4.46 is the avergae PWR without our script running
    c_energy =  time.*m_pwr/1000; %milliwatt-hour
    ylim([0, 1.6]);
end

%tiledlayout(1,2)

%nexttile
yyaxis left
%bar1 = bar(x, m_pwr);
%bar2 = bar(x*3+1, time, width);
% Online: #A4E6FF [alt: CEFFF6], Offline: #FFB5CF [alt: F7E1FC]
bar1 = bar(x(1), m_pwr(1),width,'FaceColor', '#F2EBBF');
bar3 = bar(x(2), m_pwr(2),width,'FaceColor', '#F3B562');
bar5 = bar(x(3), m_pwr(3),width,'FaceColor', '#8CBEB2');
%bar1 = bar(x,m_pwr,width,'FaceColor', '[0.3020    0.7451    0.9333]')
axis square;
box on;
grid on;
set(gca, 'FontSize', 24);
set(gca,'YMinorTick','on', 'YMinorGrid','on');
ylabel("Power (W)","Color","#000000")
xlim([0 + 0.3, 7 - 0.3 + distanceapart]);
%ylim([5, 25]);

text_font_size = 22
text_offset = 0.01
text(x(1), m_pwr(1) + text_offset, num2str(round(m_pwr(1), 2)), 'FontSize' , text_font_size, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');
text(x(2), m_pwr(2) + text_offset, num2str(round(m_pwr(2), 2)), 'FontSize' , text_font_size, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');
text(x(3), m_pwr(3) + text_offset, num2str(round(m_pwr(3), 3)), 'FontSize' , text_font_size, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');


%nexttile
yyaxis right
hold on;
% Online: #A4E6FF [alt: CEFFF6], Offline: #FFB5CF [alt: F7E1FC]
bar2 = bar(x(4), c_energy(1),width,'FaceColor', '#F2EBBF');
bar4 = bar(x(5), c_energy(2),width,'FaceColor','#F3B562' );
bar6 = bar(x(6), c_energy(3),width,'FaceColor','#8CBEB2' );
%bar3 = bar(x, c_energy,width);
%ylim([50, 550]);
text_offset = 0.01
text(x(4), c_energy(1) + text_offset, num2str(round(c_energy(1), 2)), 'FontSize' , text_font_size, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');
text(x(5), c_energy(2) + text_offset, num2str(round(c_energy(2), 2)), 'FontSize' , text_font_size, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');
text(x(6), c_energy(3) + text_offset, num2str(round(c_energy(3), 3)), 'FontSize' , text_font_size, 'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');

legend(scheme,'location', 'NorthEast')
axis square;
grid on;
set(gca, 'FontSize', 24);
set(gca,'YMinorTick','on', 'YMinorGrid','on');
%set(gca, 'YScale', 'log')
%title('')
ylim([0, 2]);
xticks([2,5 + distanceapart])
xticklabels(["Power" "Energy"])
ylabel("Energy (mWh)","Color","k")