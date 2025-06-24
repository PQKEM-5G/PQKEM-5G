% 1 for x25519
% 2 for secp256r1
% 3 for key_generation_Kyber
% 4 for publickeygen
% 5 for sharedkeygen(UE)
% 6 for sharedkeygen(HN)
% 7 for PubkG_mini
% 8 for sharedKG_mini
% 9 for PubKG_RPi
% 10 for sharedKG_RPi
plotNum = 7
fontSize = 16
textFontSize = 14
textYOffset = 2
if plotNum == 1
    data = readmatrix('x25519.csv')
elseif plotNum == 2
    data = readmatrix('secp256r1.csv')
elseif plotNum == 3
    data = readmatrix('key_generation_Kyber.csv')
elseif plotNum == 4
    data = readmatrix('pubKG_Laptop.csv')
elseif plotNum == 5
    data = readmatrix('SharedKG(UE)_Laptop.csv')
elseif plotNum == 6
    data = readmatrix('SharedKG(CN)_Laptop.csv')
elseif plotNum == 7
    data = readmatrix('PubKG_Mini.csv')
elseif plotNum == 8
    data = readmatrix('SharedKG(UE)_Mini.csv')
elseif plotNum == 9
    data = readmatrix('PubKG_RPi.csv')
elseif plotNum == 10
    data = readmatrix('SharedKG(UE)_RPi.csv')
end
x = [2, 1, 3]
y1 = data(:, 1)
y2 = data(:, 2)
y3 = data(:, 3)
y1 = y1(~isnan(y1))
y2 = y2(~isnan(y2))
y3 = y3(~isnan(y3))
avg1 = mean(y1, 1, 'omitnan')
avg2 = mean(y2, 1, 'omitnan')
avg3 = mean(y3, 1, 'omitnan')
yci1 = getConfidenceInterval(y1)
yci2 = getConfidenceInterval(y2)
yci3 = getConfidenceInterval(y3)
hold on;
% Colors from: https://color.adobe.com/explore?page=2
bar1 = bar(x(1), avg1, 'DisplayName', 'Shared Key (UE)', 'FaceColor', '#F3B562');
bar2 = bar(x(2), avg2, 'DisplayName', 'Public Key (UE)', 'FaceColor', '#F2EBBF');
bar3 = bar(x(3), avg3, 'DisplayName', 'Shared Key (CN)', 'FaceColor', '#8CBEB2');
bars = [bar1, bar2, bar3]
plotConfidenceInterval(x(1), avg1, yci1)
plotConfidenceInterval(x(2), avg2, yci2)
plotConfidenceInterval(x(3), avg3, yci3)
text(x(1), avg1 + textYOffset, num2str(avg1, '%.4g'), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'baseline', 'FontSize', textFontSize)
text(x(2), avg2 + textYOffset, num2str(avg2, '%.4g'), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'baseline', 'FontSize', textFontSize)
text(x(3), avg3 + textYOffset, num2str(avg3, '%.4g'), 'HorizontalAlignment', 'center', 'VerticalAlignment', 'baseline', 'FontSize', textFontSize)
xticks([1,2,3])
xticklabels({'secp256r1', 'x25519', 'Kyber'})
%legend(bars, 'location', 'NorthEast')
% Some extra formatting to make it pretty :)
axis square;
grid on;
box on;
set(gca, 'FontSize', fontSize);
set(gca, 'XMinorTick','off', 'XMinorGrid','off', 'YMinorTick','on', 'YMinorGrid','on');
xlim([0 + 0.3, length(x) + 1 - 0.3]);
% if plotNum == 1
%     ylim([30, 40]);
% elseif plotNum == 2
%     ylim([60, 100]);
% elseif plotNum == 3
%     ylim([0, 25]);
% end
ylim([0, 50]);
ylabel('Time Duration (\mu{s})')
function CI = getConfidenceInterval(x)
    confidence_interval_percent=0.95
    SEM = std(x)/sqrt(length(x)); % Standard Error
    tscore = tinv([1-confidence_interval_percent  confidence_interval_percent],length(x)-1);
    CI = max(tscore*SEM);
    return;
end
function plotConfidenceInterval(x, y, yci)
    ci_color = 'black'
    ci_width = 0.1
    line_thickness = 3
    plot([x - ci_width, x + ci_width], [y - yci, y - yci], 'Color', ci_color, 'LineWidth', line_thickness, 'HandleVisibility','off');
    plot([x - ci_width, x + ci_width], [y + yci, y + yci], 'Color', ci_color, 'LineWidth', line_thickness, 'HandleVisibility','off');
    plot([x, x], [y - yci, y + yci], 'Color', ci_color, 'LineWidth', line_thickness, 'HandleVisibility','off');
    
    % Add a dot in the center
    % plot(x, y, '.', 'Color', ci_color, 'MarkerSize', line_thickness*10, 'HandleVisibility', 'off')
end