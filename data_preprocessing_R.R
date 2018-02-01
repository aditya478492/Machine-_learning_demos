dataset=read.csv('Data.csv')
dataset$Age=ifelse(is.na(dataset$Age)==TRUE,ave(dataset$Age,FUN = function(x)mean(x,na.rm = TRUE)),dataset$Age);
dataset$Salary=ifelse(is.na(dataset$Salary)==TRUE,ave(dataset$Salary,FUN = function(x)mean(x,na.rm=TRUE)),dataset$Salary);

dataset$Country=factor(dataset$Country,c('France','Germany','Spain'),c(1,2,3));
dataset$Purchased=factor(dataset$Purchased,c('No','Yes'),c(0,1));

library(caTools)
set.seed(123);
split1=sample.split(dataset$Purchased,SplitRatio = 0.8);
Training_set=subset(dataset,split1==TRUE);
Test_set=subset(dataset,split1==FALSE);

#feature Scaling
Training_set[,2:3]=scale(Training_set[,2:3]);
Test_set[,2:3]=scale(Test_set[,2:3]);
