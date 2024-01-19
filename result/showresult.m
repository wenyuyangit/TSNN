close all
%% Forest
load('D:\Forest\Patch1_CHM_9layer_400_0.0001_nc.mat');
CHM_patch1 = reshape(labels,300,300); 
pred_nc_2D = reshape(pred,300,300); 
figure;
figure_fontsize = 18;
subplot(1,2,1); imagesc(CHM_patch1,[16,33]); title('Reference');
set(gca,'FontName','Times New Roman','FontSize',figure_fontsize); axis equal tight;
subplot(1,2,2); imagesc(pred_nc_2D,[16,33]); title('Prediction');
set(gca,'FontName','Times New Roman','FontSize',figure_fontsize); axis equal tight;
set(gcf,'color','w'); 
export_fig('Forest.png');

lines_arr = [1,170,280];
for mm = 1:length(lines_arr)
    lines1 = lines_arr(mm);   
    figure; 
    plot(CHM_patch1(lines1,:),'-r','linewidth',1.2);hold on;
    plot(pred_nc_2D(lines1,:),'-b','linewidth',2.2);hold on;
    grid on; set(gca,'YLim',[20,35]);xlabel('Range');
    set(gcf,'Position',[60,60,400,380]);
    set(gca,'Position',[0.13 0.17 0.80 0.74] );
    figure_fontsize = 18;
    set(gca,'FontName','Times New Roman','FontSize',figure_fontsize); 
    set(get(gca,'XLabel'),'FontSize',figure_fontsize,'Vertical','top');
    set(get(gca,'YLabel'),'FontSize',figure_fontsize,'Vertical','middle');
    set(findobj('FontSize',10),'FontSize',figure_fontsize)
    set(findobj(get(gca,'Children'),'LineWidth',0.5),'LineWidth',2);
    set(gcf,'color','w'); 
    legend('Reference','Prediction')
    export_fig(['Forest_line_',num2str(lines1),'.png']);

end

%% Ground
load('D:\Ground\Patch2_DTM_9layer_400_0.0001_nc.mat')
DTM_patch2 = reshape(labels,300,300); 
pred_nc_2D = reshape(pred,300,300); 
figure;
figure_fontsize = 18;
subplot(1,2,1); imagesc(DTM_patch2,[1,33]); title('Reference'); 
set(gca,'FontName','Times New Roman','FontSize',figure_fontsize); axis equal tight;
subplot(1,2,2); imagesc(pred_nc_2D,[1,33]); title('Prediction'); 
set(gca,'FontName','Times New Roman','FontSize',figure_fontsize); axis equal tight;
set(gcf,'color','w'); 
export_fig('Ground.png');
lines_arr = [100,150,280];
for mm = 1:length(lines_arr)
    lines1 = lines_arr(mm);   
    figure; 
    plot(DTM_patch2(lines1,:),'-r','linewidth',1.2);hold on;
    plot(pred_nc_2D(lines1,:),'-b','linewidth',2.2);hold on;
    grid on; set(gca,'YLim',[1,45]);xlabel('Range');
    set(gcf,'Position',[60,60,400,380]);
    set(gca,'Position',[0.13 0.17 0.80 0.74] );
    figure_fontsize = 18;
    set(gca,'FontName','Times New Roman','FontSize',figure_fontsize); 
    set(get(gca,'XLabel'),'FontSize',figure_fontsize,'Vertical','top');
    set(get(gca,'YLabel'),'FontSize',figure_fontsize,'Vertical','middle');
    set(findobj('FontSize',10),'FontSize',figure_fontsize)
    set(findobj(get(gca,'Children'),'LineWidth',0.5),'LineWidth',2);
    set(gcf,'color','w'); 
    legend('Reference','Prediction')
    export_fig(['Ground_line_',num2str(lines1),'.png']);
end