# kalman-filter-1D
Below is a simple program in 1D that implements the recursive idea of predict and update in Kalman Filter using the following ideas
   
 Gaussian distribution: continuous function over the space of locations and the area underneath sumps up to 1. Defined by the mean and variance
<img width="140" alt="Screen Shot 2022-06-08 at 2 29 14 PM" src="https://user-images.githubusercontent.com/90353674/172690428-7a56c791-f713-42ea-9734-31c25859f13f.png">
Variance measures how far each number in the set if from the mean and thus from every other number in the set, typically is the uncertainty
covariance measures how much two random variables vary together ex: try to predict the location of the car with the most certainty:
We try to have a Gaussian distribution with mean is the location and smallest variance<img width="507" alt="Screen Shot 2022-06-08 at 2 29 34 PM" src="https://user-images.githubusercontent.com/90353674/172690484-be7bd4e4-b22a-4634-b76d-f17b8f213ca6.png">
