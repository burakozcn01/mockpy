# MockPy

🚀 Comprehensive Realistic Data Generation Library

[![PyPI version](https://img.shields.io/badge/pypi-1.0-blue.svg)](https://pypi.org/project/mockpy/)
[![Python versions](https://img.shields.io/badge/python-3.7%2B-brightgreen.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

MockPy is a Python library for generating realistic and comprehensive mock data for testing, development, and demonstration purposes.

## 🌟 Features

- 📊 **Realistic Data**: Based on real-world distributions
- 🔄 **Cross-Data Consistency**: Related data fields maintain logical relationships
- 🧩 **Easy-to-Use API**: Intuitive design for developer productivity
- 🔌 **Framework Integration**: Works with Django, Flask, FastAPI, SQLAlchemy
- 🚀 **Performance Optimized**: Fast generation with minimal resource usage
- 🌍 **Multi-Language Support**: Built-in support for English and Turkish with translation capabilities

## 📦 Installation

```bash
pip install python-mockpy
```

## 🚀 Quick Start

```python
from mockpy import MockPy

# Initialize the library
mock = MockPy(locale="en_US")

# Generate a person
person = mock.person.person()
print(f"Hello, my name is {person.full_name}")

# Generate an address
address = mock.address.address()
print(f"My address: {address.street}, {address.city}")

# Generate credit card
credit_card = mock.finance.credit_card()
print(f"My card: {credit_card.formatted_number}")
```

## 📋 Data Types

MockPy can generate a wide variety of data:

- 👤 **Personal Information**: Names, addresses, phone numbers, emails
- 💼 **Business Data**: Company names, job titles, departments
- 💰 **Financial Data**: Bank accounts, credit cards, IBAN numbers
- 🌐 **Internet**: URLs, IP addresses, usernames
- 🏥 **Healthcare**: Patient records, diagnoses, medication names
- 🗺️ **Geographic**: GPS coordinates, countries, cities
- 🛒 **E-commerce**: Products, prices, orders
- 📚 **Education**: Schools, courses, grades

And many more!

## 🛠️ Advanced Usage

### Schema-Based Data Generation

```python
schema = {
    "id": {"type": "integer", "min": 1000, "max": 9999},
    "user": "person.person",
    "subscription": {
        "plan": {"type": "choice", "choices": ["Basic", "Premium", "Enterprise"]},
        "start_date": {"type": "date", "start": "2022-01-01", "end": "2023-01-01"},
        "price": {"type": "float", "min": 9.99, "max": 99.99, "precision": 2},
    }
}

# Generate 100 records
dataset = mock.generate_dataset(schema, count=100)
```

### JSON Schema/OpenAPI Integration

```python
# Generate data from JSON Schema
from mockpy.integrations import from_json_schema

schema_file = "user_schema.json"
users = from_json_schema(schema_file, count=50)
```

### Django Integration

```python
from mockpy.integrations.django import generate_model_instances
from myapp.models import User

# Create 10 instances of your Django model
users = generate_model_instances(User, count=10)
```

## 🌍 Multi-Language Support

```python
# English data generation
en_mock = MockPy(locale="en_US")
en_person = en_mock.person.person()

# Turkish data generation
tr_mock = MockPy(locale="tr_TR")
tr_person = tr_mock.person.person()

# Other languages (requires 'translators' package)
fr_mock = MockPy(locale="fr_FR")
fr_person = fr_mock.person.person()
```

## 🧪 Testing Use Cases

```python
def test_user_registration():
    mock = MockPy()
    test_user = mock.person.person()
    
    response = client.post('/register', data={
        'email': test_user.email,
        'name': test_user.full_name,
        'phone': test_user.phone
    })
    
    assert response.status_code == 200
```

## 🔧 Performance Considerations

MockPy is designed to be fast and resource-efficient:

- No external dependencies required for core functionality
- Minimal memory footprint
- Optimized for bulk data generation
- Smart caching for frequently used data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 💬 Contact

Project Link: [https://github.com/burakozcn01/mockpy](https://github.com/burakozcn01/mockpy)