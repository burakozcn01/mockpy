#!/usr/bin/env python
"""
MockPy Flask Demo - API Ön Yüzü

Bu örnek, MockPy kütüphanesini Flask ile entegre ederek bir API oluşturur.
Bu API, gerçekçi sahte veri üretmek için kullanılabilir.

Gereksinimler:
    - python-mockpy
    - flask

Kurulum:
    pip install python-mockpy flask

Çalıştırma:
    python mockpy_flask_app.py
"""

from flask import Flask, jsonify, request, render_template_string
from mockpy import MockPy
import random
import json

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MockPy API Demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding: 20px;
            background-color: #f8f9fa;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
        }
        pre {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .endpoint-card {
            margin-bottom: 20px;
            border-left: 4px solid #0d6efd;
        }
        h1 {
            color: #0d6efd;
        }
        .btn-primary {
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mb-4">MockPy API Demo</h1>
        <p class="lead">Bu API, python-mockpy kütüphanesi ile gerçekçi test verileri oluşturur.</p>
        
        <div class="row mt-4">
            <div class="col-md-8">
                <div class="card endpoint-card">
                    <div class="card-body">
                        <h5 class="card-title">Kullanılabilir Endpointler</h5>
                        <div class="list-group mt-3">
                            <a href="/api/person?locale=tr_TR" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                                GET /api/person
                                <span class="badge bg-primary rounded-pill">Kişi Verisi</span>
                            </a>
                            <a href="/api/people?count=5&locale=tr_TR" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                                GET /api/people?count=5
                                <span class="badge bg-primary rounded-pill">Çoklu Kişiler</span>
                            </a>
                            <a href="/api/address?locale=tr_TR" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                                GET /api/address
                                <span class="badge bg-primary rounded-pill">Adres</span>
                            </a>
                            <a href="/api/company?locale=tr_TR" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                                GET /api/company
                                <span class="badge bg-primary rounded-pill">Şirket</span>
                            </a>
                            <a href="/api/credit-card?locale=tr_TR" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                                GET /api/credit-card
                                <span class="badge bg-primary rounded-pill">Kredi Kartı</span>
                            </a>
                            <a href="/api/custom?locale=tr_TR" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                                GET /api/custom
                                <span class="badge bg-primary rounded-pill">Özel Veri</span>
                            </a>
                        </div>
                        
                        <div class="mt-4">
                            <h6 class="mb-2">Parametreler:</h6>
                            <ul>
                                <li><code>locale</code> - Dil ayarı (tr_TR, en_US, vb.)</li>
                                <li><code>count</code> - Veri sayısı (çoklu sonuçlar için)</li>
                                <li><code>seed</code> - Sabit sonuçlar için seed değeri</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">API Test</h5>
                        <form id="testForm">
                            <div class="mb-3">
                                <label for="endpoint" class="form-label">Endpoint</label>
                                <select class="form-select" id="endpoint">
                                    <option value="/api/person">Kişi</option>
                                    <option value="/api/people">Çoklu Kişiler</option>
                                    <option value="/api/address">Adres</option>
                                    <option value="/api/company">Şirket</option>
                                    <option value="/api/credit-card">Kredi Kartı</option>
                                    <option value="/api/custom">Özel Veri</option>
                                </select>
                            </div>
                            <div class="mb-3">
                                <label for="locale" class="form-label">Dil</label>
                                <select class="form-select" id="locale">
                                    <option value="tr_TR">Türkçe (tr_TR)</option>
                                    <option value="en_US">İngilizce (en_US)</option>
                                </select>
                            </div>
                            <div class="mb-3" id="countGroup">
                                <label for="count" class="form-label">Adet</label>
                                <input type="number" class="form-control" id="count" min="1" max="100" value="5">
                            </div>
                            <button type="submit" class="btn btn-primary w-100">API'yi Test Et</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="card mt-4">
            <div class="card-body">
                <h5 class="card-title">Sonuç</h5>
                <pre id="result">Henüz sonuç yok. Bir endpoint seçin ve "API'yi Test Et" butonuna tıklayın.</pre>
            </div>
        </div>
        
        <div class="alert alert-info mt-4">
            <h5>MockPy Hakkında</h5>
            <p>
                python-mockpy, gerçekçi test verileri oluşturmak için python kütüphanesidir.
                Daha fazla bilgi için <a href="https://github.com/burakozcn01/mockpy" target="_blank">GitHub</a> sayfasını ziyaret edin.
            </p>
        </div>
    </div>
    
    <script>
        document.getElementById('testForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const endpoint = document.getElementById('endpoint').value;
            const locale = document.getElementById('locale').value;
            
            let url = `${endpoint}?locale=${locale}`;
            
            if (endpoint === '/api/people') {
                const count = document.getElementById('count').value;
                url += `&count=${count}`;
            }
            
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result').textContent = JSON.stringify(data, null, 2);
                })
                .catch(error => {
                    document.getElementById('result').textContent = `Hata: ${error.message}`;
                });
        });
        
        // Count alanını sadece "people" endpoint'i seçildiğinde göster
        document.getElementById('endpoint').addEventListener('change', function() {
            document.getElementById('countGroup').style.display = 
                this.value === '/api/people' ? 'block' : 'none';
        });
        
        // Sayfa yüklendiğinde kontrol et
        window.onload = function() {
            document.getElementById('countGroup').style.display = 
                document.getElementById('endpoint').value === '/api/people' ? 'block' : 'none';
        };
    </script>
</body>
</html>
"""

mock_instances = {}

def get_mock_instance(locale="tr_TR", seed=None):
    """Belirli bir locale için MockPy örneği döndürür (gerekirse oluşturur)"""
    key = f"{locale}_{seed}"
    if key not in mock_instances:
        mock_instances[key] = MockPy(locale=locale, seed=seed)
    return mock_instances[key]

@app.route('/')
def index():
    """Ana sayfa - API dokümentasyonu"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/person')
def get_person():
    """Rastgele kişi verisi döndürür"""
    locale = request.args.get('locale', 'tr_TR')
    seed = request.args.get('seed', None)
    if seed:
        seed = int(seed)
    
    mock = get_mock_instance(locale, seed)
    person = mock.person.person(include_address=True)
    
    return jsonify(person.to_dict())

@app.route('/api/people')
def get_people():
    """Birden fazla rastgele kişi verisi döndürür"""
    locale = request.args.get('locale', 'tr_TR')
    count = int(request.args.get('count', 10))
    seed = request.args.get('seed', None)
    if seed:
        seed = int(seed)
    
    # Maksimum sayıyı sınırla
    count = min(count, 100)
    
    mock = get_mock_instance(locale, seed)
    
    people = []
    for _ in range(count):
        person = mock.person.person(include_address=True)
        people.append(person.to_dict())
    
    return jsonify(people)

@app.route('/api/address')
def get_address():
    """Rastgele adres verisi döndürür"""
    locale = request.args.get('locale', 'tr_TR')
    seed = request.args.get('seed', None)
    if seed:
        seed = int(seed)
    
    mock = get_mock_instance(locale, seed)
    address = mock.address.address()
    
    # Koordinatları ekle
    address_dict = address.to_dict()
    address_dict['coordinates'] = mock.address.coordinates()
    
    return jsonify(address_dict)

@app.route('/api/company')
def get_company():
    """Rastgele şirket verisi döndürür"""
    locale = request.args.get('locale', 'tr_TR')
    seed = request.args.get('seed', None)
    if seed:
        seed = int(seed)
    
    mock = get_mock_instance(locale, seed)
    company = mock.company.company()
    
    return jsonify(company.to_dict())

@app.route('/api/credit-card')
def get_credit_card():
    """Rastgele kredi kartı verisi döndürür"""
    locale = request.args.get('locale', 'tr_TR')
    seed = request.args.get('seed', None)
    if seed:
        seed = int(seed)
    
    mock = get_mock_instance(locale, seed)
    credit_card = mock.finance.credit_card()
    
    return jsonify(credit_card.to_dict())

@app.route('/api/custom')
def get_custom_data():
    """Özel ve karmaşık veri yapısı döndürür"""
    locale = request.args.get('locale', 'tr_TR')
    seed = request.args.get('seed', None)
    if seed:
        seed = int(seed)
    
    mock = get_mock_instance(locale, seed)
    
    # E-ticaret şeması oluştur
    schema = {
        "product_id": {"type": "integer", "min": 1000, "max": 9999},
        "name": {"type": "lorem", "words": 3},
        "description": {"type": "lorem", "paragraphs": 1},
        "price": {"type": "float", "min": 9.99, "max": 999.99, "precision": 2},
        "category": {"type": "choice", "choices": ["Electronics", "Home", "Clothing", "Sports", "Books"]},
        "availability": {
            "in_stock": {"type": "choice", "choices": [True, False]},
            "quantity": {"type": "integer", "min": 0, "max": 100},
            "estimated_delivery": {"type": "date", "start": "2023-01-01", "end": "2023-12-31"}
        },
        "seller": "company.company",
        "ratings": {
            "average": {"type": "float", "min": 1.0, "max": 5.0, "precision": 1},
            "count": {"type": "integer", "min": 0, "max": 1000}
        }
    }
    
    # 3 adet ürün üret
    products = mock.generate_dataset(schema, count=3)
    
    # Benzersiz bir ID ile sarıp döndür
    result = {
        "request_id": mock.random_element(["REQ", "API", "TXN"]) + "-" + "".join(random.choices("0123456789ABCDEF", k=8)),
        "timestamp": mock.datetime.iso8601(),
        "products": products
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)