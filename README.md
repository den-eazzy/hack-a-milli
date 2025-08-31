# DotKE 🇰🇪

> **Simplifying .KE domain registration for Kenya**

DotKE is a comprehensive platform that streamlines the process of searching for and registering `.KE` domains in Kenya. Available as both a web application and Android mobile app, DotKE provides real-time domain availability checks and direct registration with authorized registrars through a single, user-friendly interface.

## 🚀 Features

- **Real-time Domain Search**: Instantly check `.KE` domain availability
- **Registrar Comparison**: View pricing, policies, and details from multiple authorized registrars
- **Direct Registration**: Initiate domain registration seamlessly through selected registrars
- **Cross-Platform Access**: Available as Flutter web app and Android APK
- **Secure Backend**: FastAPI-powered with EPP protocol integration
- **Mobile-First Design**: Optimized for on-the-go domain management

## 🎯 Who It's For

- **Entrepreneurs & Startups** establishing their online presence in Kenya
- **Web Developers & Designers** seeking reliable `.KE` domains for clients
- **Businesses** looking for fast, transparent domain registration
- **Anyone** wanting to secure a local Kenyan domain without navigating multiple registrar websites

## 🛠️ Technology Stack

### Frontend
- **Flutter** - Cross-platform framework for web and Android
- Responsive design optimized for all screen sizes

### Backend
- **Python** with **FastAPI** - High-performance REST API
- **SQLite** - Lightweight database for domain and registrar data
- **EPP Protocol** - Extensible Provisioning Protocol for registrar communication
- **python-dotenv** - Environment configuration management

### Infrastructure
- **Nginx/Apache** - Web server deployment
- **CORS Support** - Cross-origin resource sharing enabled

## 📱 Platform Availability

| Platform | Status | Download |
|----------|--------|----------|
| Web App | ✅ Available | [Visit DotKE Web](/) |
| Android APK | ✅ Available | [Download APK](#) |
| iOS | 🔄 Coming Soon | - |

## 🏗️ Installation & Setup

### Prerequisites
- Python 3.8+
- Flutter SDK
- Android Studio (for APK building)

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/dotke.git
   cd dotke
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Initialize database**
   ```bash
   python -m backend.database.init_db
   ```

5. **Start the API server**
   ```bash
   uvicorn backend.main:app --reload
   ```

### Frontend Setup

1. **Install Flutter dependencies**
   ```bash
   cd frontend
   flutter pub get
   ```

2. **Run web application**
   ```bash
   flutter run -d chrome
   ```

3. **Build Android APK**
   ```bash
   flutter build apk --release
   ```

## 🔧 API Endpoints

### Domain Operations
- `GET /domains/search?q={domain}` - Search domain availability
- `GET /domains/registrars` - List authorized registrars
- `POST /domains/register` - Initiate domain registration

### Registrar Operations
- `GET /registrars` - Get all registrar information
- `GET /registrars/{id}` - Get specific registrar details

## 🔄 How It Works

1. **Search**: Users enter desired domain name via web or mobile interface
2. **Query**: FastAPI backend checks availability using EPP protocol
3. **Results**: Real-time display of availability with registrar options and pricing
4. **Register**: Users select preferred registrar and initiate secure registration
5. **Confirmation**: Backend manages API calls and provides registration status

## 📊 Project Structure

```
dotke/
├── backend/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── main.py
├── frontend/
│   ├── lib/
│   ├── assets/
│   └── pubspec.yaml
├── docs/
├── tests/
└── README.md
```

## 🚨 Important Limitations

- **Domain Registration Only**: This platform handles domain search and initial registration
- **No Renewal Services**: Domain renewals are not supported through this platform
- **Kenya-Specific**: Focused exclusively on `.KE` domain extensions

## 🤝 Contributing

We welcome contributions to improve DotKE! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check our [API docs](docs/api.md) and [setup guide](docs/setup.md)
- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/your-username/dotke/issues)
- **Contact**: [your-email@domain.com](mailto:your-email@domain.com)

## 🙏 Acknowledgments

- Kenya's Communications Authority for `.KE` domain policies
- Authorized `.KE` registrars for API collaboration
- Flutter and FastAPI communities for excellent documentation

---

**Made with ❤️ for the Kenyan tech community**

*Empowering local businesses and entrepreneurs to establish their digital presence with ease.*
