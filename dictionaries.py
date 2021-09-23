
month_conversion = {
  "Jan":"January",
  "Feb":"February",
  "Mar":"March",
  "Apr":"April",
  "May":"May",
  "Jun":"June",
  "Jul":"July",
  "Aug":"August",
  "Sep":"September",
  "Oct":"October",
  "Nov":"November",
  "Dec":"December"
}

print(month_conversion["Jan"]) # gets value from key, error if key not valid
print(month_conversion.get("Feb")) # gets value from key but no error shown
print(month_conversion.get("Hue","Not valid")) # get with error handler

