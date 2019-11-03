clear
set more off

cd "C:\Users\trent\Dropbox\GitHub\Forecasting"
import delimited "champagne.csv", clear 

// replace startdate="0"+startdate if substr(startdate,2,1)=="/"
// replace startdate = substr(startdate,1,3) + "0" + substr(startdate,4,.) if substr(startdate,5,1) == "/"
gen str4 dxyr= substr(month,1,4)
gen str2 dxmo = substr(month,6,7)

destring dx*, replace
gen double Date = ym(dxyr, dxmo)
drop month

tsset Date
//twoway (tsline sales)


** Naive Persistence Forecast
reg sale L.sales
reg sales L.sales i.dxmo i.dxyr if Date<141

predict saleshat_naive

twoway (tsline sales)(tsline saleshat_naive)

** ARIMA
gen sales2 = sales
gen lag1 = sales[_n-12]   //seasonal lag
replace sales2 = sales2 - lag1
line sales2 Date

dfuller sales2 if Date<141, lags(0) // t-stat=-7.6 < 1%cv=-3.5 ==> stationary

ac sales2 if Date<141
pac sales2 if Date<141

arima sales2 if Date<141, arima(0,0,1)
predict saleshat_arima
replace saleshat_arima=saleshat_arima+lag1
twoway (tsline sales)(tsline saleshat_arima)
