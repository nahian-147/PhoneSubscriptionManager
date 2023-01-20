def assignNewPhoneNumber(lastPhoneNumberSuffix):
    
    countryCode = '+880'
    mobileCompanyCode = '18'
    
    prefix = countryCode + mobileCompanyCode

    suffix = str(int(lastPhoneNumberSuffix) +1)

    phoneNumber = prefix+suffix

    if len(phoneNumber) == 14:
        return phoneNumber
    else:
        return None

    