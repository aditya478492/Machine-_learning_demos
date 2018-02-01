dataset=read.csv('50_Startups.csv')

#converting categorical to numerical
dataset$State=factor(dataset$State,labels = c(1,2,3))

#splitng training and test sets
set.seed(123)
split1=sample.split(dataset$Profit,SplitRatio=0.8)
training_set=subset(dataset,split1==TRUE)
test_set=subset(dataset,split1==FALSE)

#fitting multiple linear regressor to model
regressor=lm(formula = Profit ~ .,data = dataset)
Y_pred=predict(regressor,data=test_set)

regressor_be=lm(formula = Profit ~ R.D.Spend,data = dataset);
Y_pred=predict(regressor_be,data=training_set)
