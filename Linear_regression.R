dataset=read.csv('Salary_Data.csv');
X=dataset$YearsExperience;
Y=dataset$Salary;

split=sample.split(dataset$YearsExperience,SplitRatio = 1/3);
training_set=subset(dataset,split==TRUE);
test_set=subset(dataset,split==FALSE);
regressor=lm(formula = Salary ~ YearsExperience,data=training_set);

Y_pred=predict(regressor,newdata = test_set);
ggplot()+
  geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),colour="red")+
  geom_line(aes(x=training_set$YearsExperience,y=predict(regressor,newdata = training_set)),colour='blue')+
  ggtitle("Years of expereince vs salary")+
  xlab("Years of Experience")+
  ylab("Salary")


