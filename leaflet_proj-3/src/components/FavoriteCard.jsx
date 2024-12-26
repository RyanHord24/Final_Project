import React from 'react';
import { Card, Button, Form } from 'react-bootstrap';
import axios from "axios";

const countryCodeMap = {
    "Andorra": "AD",
    "United Arab Emirates": "AE",
    "Afghanistan": "AF",
    "Antigua and Barbuda": "AG",
    "Anguilla": "AI",
    "Albania": "AL",
    "Armenia": "AM",
    "Netherlands Antilles": "AN",
    "Angola": "AO",
    "Antarctica": "AQ",
    "Argentina": "AR",
    "American Samoa": "AS",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Åland Islands": "AX",
    "Azerbaijan": "AZ",
    "Bosnia and Herzegovina": "BA",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Belgium": "BE",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Bahrain": "BH",
    "Burundi": "BI",
    "Benin": "BJ",
    "Saint Barthélemy": "BL",
    "Bermuda": "BM",
    "Brunei Darussalam": "BN",
    "Bolivia": "BO",
    "Bonaire, Sint Eustatius and Saba": "BQ",
    "Brazil": "BR",
    "Bahamas": "BS",
    "Bhutan": "BT",
    "Bouvet Island": "BV",
    "Botswana": "BW",
    "Belarus": "BY",
    "Belize": "BZ",
    "Canada": "CA",
    "Cocos (Keeling) Islands": "CC",
    "Congo, The Democratic Republic Of The": "CD",
    "Central African Republic": "CF",
    "Congo": "CG",
    "Switzerland": "CH",
    "Côte D'Ivoire": "CI",
    "Cook Islands": "CK",
    "Chile": "CL",
    "Cameroon": "CM",
    "China": "CN",
    "Colombia": "CO",
    "Costa Rica": "CR",
    "Cuba": "CU",
    "Cape Verde": "CV",
    "Curaçao": "CW",
    "Christmas Island": "CX",
    "Cyprus": "CY",
    "Czech Republic": "CZ",
    "Germany": "DE",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Algeria": "DZ",
    "Ecuador": "EC",
    "Estonia": "EE",
    "Egypt": "EG",
    "Western Sahara": "EH",
    "Eritrea": "ER",
    "Spain": "ES",
    "Ethiopia": "ET",
    "Finland": "FI",
    "Fiji": "FJ",
    "Falkland Islands (Malvinas)": "FK",
    "Micronesia, Federated States Of": "FM",
    "Faroe Islands": "FO",
    "France": "FR",
    "Gabon": "GA",
    "United Kingdom": "GB",
    "Grenada": "GD",
    "Georgia": "GE",
    "French Guiana": "GF",
    "Guernsey": "GG",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greenland": "GL",
    "Gambia": "GM",
    "Guinea": "GN",
    "Guadeloupe": "GP",
    "Equatorial Guinea": "GQ",
    "Greece": "GR",
    "South Georgia and the South Sandwich Islands": "GS",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Hong Kong": "HK",
    "Heard and McDonald Islands": "HM",
    "Honduras": "HN",
    "Croatia": "HR",
    "Haiti": "HT",
    "Hungary": "HU",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Israel": "IL",
    "Isle of Man": "IM",
    "India": "IN",
    "British Indian Ocean Territory": "IO",
    "Iraq": "IQ",
    "Iran, Islamic Republic Of": "IR",
    "Iceland": "IS",
    "Italy": "IT",
    "Jersey": "JE",
    "Jamaica": "JM",
    "Jordan": "JO",
    "Japan": "JP",
    "Kenya": "KE",
    "Kyrgyzstan": "KG",
    "Cambodia": "KH",
    "Kiribati": "KI",
    "Comoros": "KM",
    "Saint Kitts And Nevis": "KN",
    "Korea, Democratic People's Republic Of": "KP",
    "Korea, Republic of": "KR",
    "Kuwait": "KW",
    "Cayman Islands": "KY",
    "Kazakhstan": "KZ",
    "Lao People's Democratic Republic": "LA",
    "Lebanon": "LB",
    "Saint Lucia": "LC",
    "Liechtenstein": "LI",
    "Sri Lanka": "LK",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Latvia": "LV",
    "Libya": "LY",
    "Morocco": "MA",
    "Monaco": "MC",
    "Moldova, Republic of": "MD",
    "Montenegro": "ME",
    "Saint Martin": "MF",
    "Madagascar": "MG",
    "Marshall Islands": "MH",
    "Macedonia, the Former Yugoslav Republic Of": "MK",
    "Mali": "ML",
    "Myanmar": "MM",
    "Mongolia": "MN",
    "Macao": "MO",
    "Northern Mariana Islands": "MP",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Montserrat": "MS",
    "Malta": "MT",
    "Mauritius": "MU",
    "Maldives": "MV",
    "Malawi": "MW",
    "Mexico": "MX",
    "Malaysia": "MY",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "New Caledonia": "NC",
    "Niger": "NE",
    "Norfolk Island": "NF",
    "Nigeria": "NG",
    "Nicaragua": "NI",
    "Netherlands": "NL",
    "Norway": "NO",
    "Nepal": "NP",
    "Nauru": "NR",
    "Niue": "NU",
    "New Zealand": "NZ",
    "Oman": "OM",
    "Panama": "PA",
    "Peru": "PE",
    "French Polynesia": "PF",
    "Papua New Guinea": "PG",
    "Philippines": "PH",
    "Pakistan": "PK",
    "Poland": "PL",
    "Saint Pierre And Miquelon": "PM",
    "Pitcairn": "PN",
    "Puerto Rico": "PR",
    "Palestine, State of": "PS",
    "Portugal": "PT",
    "Palau": "PW",
    "Paraguay": "PY",
    "Qatar": "QA",
    "Réunion": "RE",
    "Romania": "RO",
    "Serbia": "RS",
    "Russian Federation": "RU",
    "Rwanda": "RW",
    "Saudi Arabia": "SA",
    "Solomon Islands": "SB",
    "Seychelles": "SC",
    "Sudan": "SD",
    "Sweden": "SE",
    "Singapore": "SG",
    "Saint Helena": "SH",
    "Slovenia": "SI",
    "Svalbard And Jan Mayen": "SJ",
    "Slovakia": "SK",
    "Sierra Leone": "SL",
    "San Marino": "SM",
    "Senegal": "SN",
    "Somalia": "SO",
    "Suriname": "SR",
    "South Sudan": "SS",
    "Sao Tome and Principe": "ST",
    "El Salvador": "SV",
    "Sint Maarten": "SX",
    "Syrian Arab Republic": "SY",
    "Swaziland": "SZ",
    "Turks and Caicos Islands": "TC",
    "Chad": "TD",
    "French Southern Territories": "TF",
    "Togo": "TG",
    "Thailand": "TH",
    "Tajikistan": "TJ",
    "Tokelau": "TK",
    "Timor-Leste": "TL",
    "Turkmenistan": "TM",
    "Tunisia": "TN",
    "Tonga": "TO",
    "Turkey": "TR",
    "Trinidad and Tobago": "TT",
    "Tuvalu": "TV",
    "Taiwan, Republic Of China": "TW",
    "Tanzania, United Republic of": "TZ",
    "Ukraine": "UA",
    "Uganda": "UG",
    "United States Minor Outlying Islands": "UM",
    "United States of America": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Holy See (Vatican City State)": "VA",
    "Saint Vincent And The Grenadines": "VC",
    "Venezuela, Bolivarian Republic of": "VE",
    "Virgin Islands, British": "VG",
    "Virgin Islands, U.S.": "VI",
    "Vietnam": "VN",
    "Vanuatu": "VU",
    "Wallis and Futuna": "WF",
    "Samoa": "WS",
    "Yemen": "YE",
    "Mayotte": "YT",
    "South Africa": "ZA",
    "Zambia": "ZM",
    "Zimbabwe": "ZW"
};

const FavoriteCard = ({ favorite, onUpdate, onDelete }) => {

    const countryCode = countryCodeMap[favorite.country.name];

    const handleDateChange = async (field, value) => {
        const authToken = localStorage.getItem('authToken');
        try {
            const response = await axios.put(
                `http://localhost:8000/api/v1/favorites/country/${favorite.country.id}/`,
                { ...favorite, [field]: value },
                {
                    headers: {
                        Authorization: `Token ${authToken}`,
                    },
                }
            );
            onUpdate(response.data); // Notify parent component about the update
        } catch (error) {
            console.error('Error updating favorite:', error);
        }
    };

    const handleAddNotebook = async () => {
        const authToken = localStorage.getItem('authToken');
        try {
            const response = await axios.post(
                "http://localhost:8000/api/v1/notebook/country/",
                { country_id: favorite.country.id }, 
                {
                    headers: {
                        Authorization: `Token ${authToken}`,
                    },
                }
            );
            console.log('New notebook created:', response.data);
        } catch (error) {
            console.error('Error adding new notebook:', error);
        }
    };

    const handleDelete = async () => {
        const authToken = localStorage.getItem('authToken');
        try {
            await axios.delete(`http://localhost:8000/api/v1/favorites/country/${favorite.country.id}/`, {
                headers: {
                    Authorization: `Token ${authToken}`,
                },
            });
            onDelete(favorite.id);
        } catch (error) {
            console.error('Error deleting favorite:', error);
        }
    };
    
    return (
        <Card style={{ width: '18rem', marginBottom: '1rem' }}>
            <Card.Img
                variant="top"
                src={`https://flagsapi.com/${countryCode}/flat/64.png`}
                alt={`${favorite.country.name} flag`}
            />
            <Card.Body>
                <Card.Title>{favorite.country.name}</Card.Title>
                <Form.Group>
                    <Form.Label>Travel Start Date</Form.Label>
                    <Form.Control
                        type="date"
                        value={favorite.travel_start_date || ''}
                        onChange={(e) => handleDateChange('travel_start_date', e.target.value)}
                    />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Travel End Date</Form.Label>
                    <Form.Control
                        type="date"
                        value={favorite.travel_end_date || ''}
                        onChange={(e) => handleDateChange('travel_end_date', e.target.value)}
                    />
                </Form.Group>
                <Button
                    variant="primary"
                    onClick={handleAddNotebook}
                    style={{ marginTop: '1rem' }}
                >
                    Add Notebook
                </Button>
                <Button variant="danger" onClick={handleDelete} style={{ marginTop: '1rem' }}>
                    Delete Favorite
                </Button>
            </Card.Body>
        </Card>
    );
};

export default FavoriteCard;