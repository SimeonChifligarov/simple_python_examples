import phonenumbers
from phonenumbers import (
    geocoder, carrier, timezone, NumberParseException, PhoneNumberFormat
)


def extract_phone_number_data(raw_number, default_region="US"):
    try:
        number = phonenumbers.parse(raw_number, default_region)
    except NumberParseException as e:
        return {"error": str(e), "input": raw_number}

    if not phonenumbers.is_possible_number(number):
        return {"error": "Number is not possible.", "input": raw_number}

    if not phonenumbers.is_valid_number(number):
        return {"error": "Number is not valid.", "input": raw_number}

    location = geocoder.description_for_number(number, "en")

    data = {
        "Input": raw_number,
        "International Format": phonenumbers.format_number(number, PhoneNumberFormat.INTERNATIONAL),
        "National Format": phonenumbers.format_number(number, PhoneNumberFormat.NATIONAL),
        "E.164 Format": phonenumbers.format_number(number, PhoneNumberFormat.E164),
        "RFC3966 Format": phonenumbers.format_number(number, PhoneNumberFormat.RFC3966),
        "Country Code": number.country_code,
        "National Number": number.national_number,
        "Region Description": location,
        "Carrier": carrier.name_for_number(number, "en"),
        "Time Zones": timezone.time_zones_for_number(number),
        "Number Type": phonenumbers.number_type(number).__str__(),
        "Is Valid": True,
        "Is Possible": True
    }

    return data


# Example usage
if __name__ == "__main__":
    raw_numbers = [
        "",
    ]

    for raw in raw_numbers:
        print(f"\n📞 Analyzing: {raw}")
        result = extract_phone_number_data(raw)
        for key, value in result.items():
            print(f"{key}: {value}")
