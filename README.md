# 🧪 Selenium Automation Testing Framework

A comprehensive automated testing framework built with Selenium, Python, and Pytest for testing the **Practice Software Testing** e-commerce website (https://practicesoftwaretesting.com).

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run Tests](#how-to-run-tests)
- [Architecture](#architecture)
- [Project Modules](#project-modules)
- [Configuration](#configuration)
- [Logs & Reports](#logs--reports)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Project Overview

This project is an **automated test suite** designed to validate the functionality of an e-commerce platform. It uses the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and readability of test code.

**Website Under Test:** https://practicesoftwaretesting.com

**Framework Stack:**
- **Language:** Python 3.x
- **Test Framework:** Pytest
- **UI Automation:** Selenium WebDriver
- **Browser Driver:** ChromeDriver (managed via webdriver-manager)

---

## ✨ Features

The test suite covers the following functional modules:

### 🔐 Authentication Module
- ✅ User login with valid credentials
- ✅ Invalid credentials validation
- ✅ User registration with unique email creation
- ✅ Google OAuth authentication

### 🔍 Search Module
- ✅ Product search by keywords
- ✅ Search results display
- ✅ Invalid search handling
- ✅ Partial keyword search

### 📊 Product Sorting Module
- ✅ Sort by Name (A-Z)
- ✅ Sort by Name (Z-A)
- ✅ Sort by Price (Low to High)
- ✅ Sort by Price (High to Low)
- ✅ Sort by Rating

### 🎯 Product Filter Module
- ✅ Filter by Category
- ✅ Filter by Brand
- ✅ Filter by Sustainability
- ✅ Multi-checkbox filtering
- ✅ Dynamic product updates

### 📦 Product Details Module
- ✅ View product details
- ✅ Quantity increase/decrease
- ✅ Minimum quantity validation
- ✅ Product information display

### 🛒 Add To Cart Module
- ✅ Add products to cart
- ✅ Dynamic cart count update
- ✅ Cart persistence
- ✅ Checkout integration

### 💳 Checkout Module
- ✅ Checkout process
- ✅ Guest checkout option
- ✅ Billing address validation
- ✅ Payment method selection
- ✅ Order confirmation

### 📞 Contact Form Module
- ✅ Contact form submission
- ✅ Field validation
- ✅ File upload (TXT format)
- ✅ Character requirement validation

### 📁 File Upload Validation Module
- ✅ TXT file acceptance
- ✅ Invalid file rejection
- ✅ File type validation

### 🗂️ Navigation Module
- ✅ Navbar category navigation
- ✅ Dropdown menu functionality
- ✅ URL verification
- ✅ Page heading validation

---

## 📂 Project Structure

```
Selenium-Project/
│
├── 📄 conftest.py                 # Pytest configuration & fixtures
├── 📄 pytest.ini                  # Pytest settings
├── 📄 README.md                   # This file
├── 📄 requirements.txt            # Project requirements & features
│
├── 📁 pages/                      # Page Object Model Classes
│   ├── base_page.py              # Base page class for common methods
│   ├── login_page.py             # Login page objects & methods
│   ├── register_page.py          # Registration page objects
│   ├── home_page.py              # Home page objects
│   ├── product_page.py           # Product detail page objects
│   ├── cart_page.py              # Shopping cart page objects
│   ├── checkout_page.py          # Checkout page objects
│   ├── search_page.py            # Search results page objects
│   ├── filter_page.py            # Product filter page objects
│   ├── sort_page.py              # Product sorting page objects
│   ├── categories_page.py        # Category navigation page objects
│   ├── contact_page.py           # Contact form page objects
│   └── google_login_page.py      # Google OAuth page objects
│
├── 📁 tests/                      # Test Cases
│   ├── test_login.py             # Login functionality tests
│   ├── test_register.py          # Registration functionality tests
│   ├── test_search.py            # Search functionality tests
│   ├── test_filter.py            # Filter functionality tests
│   ├── test_sort.py              # Sorting functionality tests
│   ├── test_price_range.py       # Price range tests
│   ├── test_add_to_cart.py       # Add to cart tests
│   ├── test_cart.py              # Cart functionality tests
│   ├── test_checkout.py          # Checkout process tests
│   ├── test_place_order.py       # Order placement tests
│   ├── test_contact_form.py      # Contact form tests
│   ├── test_categories_navbar.py # Navigation tests
│   └── test_google_login.py      # Google OAuth tests
│
├── 📁 utils/                      # Utility Classes
│   ├── driver_factory.py         # WebDriver initialization
│   ├── logger.py                 # Logging configuration
│   └── config_reader.py          # Configuration reader (for future use)
│
├── 📁 data/                       # Test Data
│   └── test_data.json            # Test data in JSON format
│
├── 📁 logs/                       # Test Logs (Generated)
│   └── test.log                  # Test execution logs
│
├── 📁 screenshots/               # Failure Screenshots (Generated)
│   └── *.png                     # Screenshots captured on test failure
│
└── 📁 reports/                   # Test Reports (Generated)
    └── [Test reports will be generated here]
```

---

## 🔧 Prerequisites

Before running the tests, ensure you have the following installed:

1. **Python 3.8+**
   - [Download Python](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Git** (Optional, for version control)
   - [Download Git](https://git-scm.com/downloads)

3. **IDE/Editor** (Recommended)
   - Visual Studio Code, PyCharm, or similar

4. **Chrome Browser**
   - The tests use Chrome browser (webdriver-manager will download the correct ChromeDriver version automatically)

---

## 📥 Installation

### Step 1: Clone the Repository (or navigate to project directory)

```bash
cd D:\Selenium-Project
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Required Packages:**
```
selenium==4.x.x
pytest==7.x.x
webdriver-manager==4.x.x
```

### Step 4: Verify Installation

```bash
pytest --version
python -c "import selenium; print(selenium.__version__)"
```

---

## 🚀 How to Run Tests

### Run All Tests

```bash
pytest
```

### Run Tests from Specific File

```bash
pytest tests/test_login.py
```

### Run Specific Test Function

```bash
pytest tests/test_login.py::test_valid_login
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run Tests with Detailed Output and Print Statements

```bash
pytest -vv -s
```

### Run Tests Matching a Pattern

```bash
pytest -k "test_login"
```

### Run Tests with Custom Report Generation

```bash
pytest --html=reports/report.html --self-contained-html
```

### Run Tests and Stop at First Failure

```bash
pytest -x
```

### Run Tests with Specific Markers

```bash
pytest -m smoke    # If markers are configured
```

### Display Test Coverage (if coverage is installed)

```bash
pytest --cov=tests/
```

---

## 🏗️ Architecture

### Page Object Model (POM)

This framework follows the **Page Object Model** design pattern:

**Benefits:**
- 🎯 **Maintainability:** Locators are centralized in page classes
- 🔄 **Reusability:** Common actions are defined once and reused
- 📖 **Readability:** Tests are easy to understand and follow business logic
- 🛡️ **Scalability:** Easy to add new pages and tests

**Structure:**

```python
# Example: pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@data-test='login-submit']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Methods
    def enter_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        element.send_keys(email)
    
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
```

**Test Usage:**

```python
# Example: tests/test_login.py
def test_valid_login(driver):
    driver.get("https://practicesoftwaretesting.com/auth/login")
    login_page = LoginPage(driver)
    login_page.login("customer@practicesoftwaretesting.com", "welcome01")
    # Assertions...
```

---

## 📦 Project Modules

### 1. **Pages Module** (`pages/`)

Contains Page Object classes for different pages of the website:

- **base_page.py:** Base class with common methods (inheritable by all pages)
- **Individual Page Classes:** Each page has its own class with:
  - Locators (By, XPATH, ID, CSS selectors)
  - Page methods for user interactions
  - Wait conditions for element availability

### 2. **Tests Module** (`tests/`)

Contains test cases organized by feature/functionality:

- Each test file corresponds to a specific feature
- Tests follow naming convention: `test_*.py`
- Tests use pytest fixtures for browser driver
- Each test is independent and can run in any order

### 3. **Utils Module** (`utils/`)

Contains helper classes and utilities:

- **driver_factory.py:** Handles WebDriver initialization and configuration
- **logger.py:** Centralized logging configuration
- **config_reader.py:** Configuration management (extendable)

### 4. **Data Module** (`data/`)

Contains test data in structured format:

- **test_data.json:** Test data for various test cases
- Used for parameterized tests

---

## 🤖 AI Integration & Use Cases

This Selenium project can be enhanced and optimized using AI and Machine Learning technologies for improved automation, testing, and maintenance.

### 1. **AI-Powered Test Generation**

AI can automatically generate test cases based on:

- **User Behavior Analysis:** AI learns from user interaction patterns and generates relevant test scenarios
- **Code Coverage Optimization:** ML algorithms identify gaps in test coverage and suggest new test cases
- **Automated Locator Generation:** AI suggests optimal element locators (XPath, CSS selectors) that are more stable

**Tools:**
- GitHub Copilot for test code suggestions
- OpenAI API for intelligent test case generation
- Pytest plugins with AI enhancements

**Example:**
```python
# AI can suggest similar test cases
# Instead of writing test_login_valid, test_login_invalid manually,
# AI generates comprehensive test variations automatically
```

### 2. **Intelligent Test Maintenance**

AI helps maintain and update tests when website structure changes:

- **Auto-Locator Repair:** ML detects broken locators and suggests fixes
- **Test Failure Analysis:** AI analyzes failure logs and recommends solutions
- **Flaky Test Detection:** ML identifies unstable tests and suggests improvements

**Benefits:**
- Reduces manual maintenance effort by 60%+
- Prevents test failures due to locator changes
- Improves test reliability

### 3. **Visual AI Testing**

Leverage AI for visual and image-based testing:

- **Screenshot Comparison:** AI compares screenshots automatically
- **Visual Regression Detection:** Identifies UI changes automatically
- **OCR-Based Validation:** Extract and validate text from images

**Tools:**
- Applitools Eyes for visual testing
- PyAutoGUI with image recognition
- OpenCV with Python

**Example:**
```python
# AI compares current screenshot with baseline
# Detects pixel-level differences
# Reports visual regressions automatically
```

### 4. **Natural Language Test Writing**

Write tests in plain English using AI:

```
Input: "User should be able to login with valid email and password"
Output: Complete test code with all steps and assertions
```

**Tools:**
- GitHub Copilot (autocomplete & suggestions)
- ChatGPT/Claude for test generation
- Codex for code-to-test conversion

### 5. **Smart Test Data Generation**

AI generates realistic test data automatically:

- **Faker Library with AI:** Generate valid emails, addresses, phone numbers
- **ML-based Data Synthesis:** Create data that matches real-world scenarios
- **Boundary Value Analysis:** AI suggests edge cases automatically

**Example:**
```python
import faker
fake = Faker()

# AI-generated realistic test data
email = fake.email()                # user12345@gmail.com
address = fake.address()            # 123 Main St, New York, NY
phone = fake.phone_number()         # +1-555-123-4567
```

### 6. **Predictive Test Failure Analysis**

AI predicts which tests will likely fail:

- **Historical Analysis:** ML learns from past test runs
- **Early Warning System:** Predicts failures before they occur
- **Resource Optimization:** Runs high-risk tests first

**Benefits:**
- Save time by running only relevant tests
- Reduce false positives
- Optimize CI/CD pipeline execution

### 7. **Intelligent Performance Optimization**

AI optimizes test execution speed:

- **Load Balancing:** Distribute tests across multiple machines
- **Execution Time Prediction:** Estimate how long tests will take
- **Parallel Test Optimization:** AI determines optimal parallel execution

**Example:**
```bash
# AI-optimized test execution
pytest --ai-optimize --parallel=4  # Uses 4 workers intelligently
```

### 8. **Anomaly Detection in Test Results**

AI detects unusual patterns in test behavior:

- **Timeout Detection:** Identifies slow-running tests
- **Resource Leaks:** Detects memory/CPU issues
- **Network Issues:** Identifies intermittent connectivity problems

### 9. **Smart Screenshot Analysis**

AI analyzes failure screenshots automatically:

- **Object Detection:** Identifies missing elements on page
- **Layout Validation:** Checks if elements are correctly positioned
- **Color & Contrast Analysis:** Validates UI appearance

**Tools:**
- TensorFlow for object detection
- OpenCV for image processing
- YOLO for real-time detection

### 10. **AI-Powered Logging & Debugging**

AI enhances logging with intelligent insights:

- **Contextual Logging:** Automatically logs relevant information
- **Root Cause Analysis:** AI traces test failures to root causes
- **Actionable Recommendations:** Suggests how to fix issues

**Example Log Output:**
```
[AI INSIGHT] Test failed due to:
  ├─ Element not visible (probability: 95%)
  ├─ Suggested fix: Increase WebDriverWait timeout from 10s to 15s
  ├─ Similar issues: 3 previous occurrences
  └─ Fix success rate: 87%
```

### 11. **Chatbot-Based Test Troubleshooting**

Use AI chatbots for quick help:

- **GitHub Copilot Chat:** Ask questions about test failures
- **Custom AI Assistant:** Train on your project specifics
- **Instant Debugging:** Get solutions in seconds

**Example:**
```
Question: "Why is test_checkout failing?"
AI Response: 
  - Payment element timeout (most likely)
  - Network latency issue (secondary)
  - Suggested solutions with code examples
```

### 12. **Self-Healing Tests**

AI automatically repairs broken tests:

- **Adaptive Locators:** AI learns alternative locator strategies
- **Auto-Retry Logic:** Intelligently retries failed steps
- **Context-Aware Fixes:** Understands page context for better fixes

**Example:**
```python
# AI detects broken locator and auto-fixes
# Old: By.XPATH, "//button[@id='old-id']"  # Element ID changed
# AI Fix: By.XPATH, "//button[contains(text(), 'Login')]"  # Uses text instead
```

---

## 🚀 Getting Started with AI Integration

### Step 1: Enable GitHub Copilot

1. Install GitHub Copilot extension in VS Code
2. Sign in with GitHub account
3. Start typing test code and Copilot will suggest completions

### Step 2: Use AI for Code Generation

```bash
# Ask Copilot to generate test
# Type: "# test to login and add product to cart"
# Copilot will suggest complete test code
```

### Step 3: Implement AI Libraries

```bash
# Install AI/ML tools
pip install faker         # Realistic data generation
pip install applitools-eyes  # Visual testing
pip install pillow        # Image processing
```

### Step 4: Enhance with Monitoring

```python
# Example: Use AI for test insights
from utils.ai_analyzer import TestAnalyzer

analyzer = TestAnalyzer()
analyzer.analyze_test_results()
analyzer.predict_failures()
analyzer.suggest_optimizations()
```

---

## 📊 AI Tools Recommended for This Project

| Tool | Purpose | Cost |
|------|---------|------|
| **GitHub Copilot** | Code completion & suggestions | $10/month |
| **Applitools Eyes** | Visual AI testing | Free + Paid |
| **OpenAI API** | Test generation & analysis | Pay-as-you-go |
| **ChatGPT Plus** | Real-time debugging help | $20/month |
| **Faker Library** | Test data generation | Free |
| **PyAutoGUI** | Image-based automation | Free |
| **TensorFlow/PyTorch** | Custom ML models | Free |

---

## 🔮 Future AI Enhancements

- [ ] Implement self-healing tests
- [ ] Add visual AI testing with Applitools
- [ ] Create AI-based test report generation
- [ ] Build ML model for test failure prediction
- [ ] Develop custom AI assistant for test debugging
- [ ] Implement automated test data generation
- [ ] Add AI-powered performance optimization

---

## ⚙️ Configuration

### conftest.py - Pytest Configuration

```python
@pytest.fixture
def driver():
    # Initialize Chrome driver
    # Configure browser settings
    # Return driver for test
    # Cleanup after test
```

**Features:**
- ✅ Automatic browser window maximization
- ✅ Implicit/Explicit waits configuration
- ✅ Automatic screenshot capture on test failure
- ✅ Browser cleanup after each test

### pytest.ini - Pytest Settings

Configure test discovery, markers, and plugins in `pytest.ini`.

### logger.py - Logging Configuration

Logs are created in the `logs/` directory:

```
logs/
└── test.log  # Contains timestamped log entries
```

**Log Format:**
```
2024-05-22 10:30:45 - INFO - Login Page Opened
2024-05-22 10:30:46 - INFO - Email Entered
2024-05-22 10:30:47 - ERROR - Element not found
```

---

## 📊 Logs & Reports

### Test Logs

Location: `logs/test.log`

Logs contain:
- Test execution flow
- User actions (navigation, clicks, input)
- Errors and exceptions
- Timestamps for performance analysis

### Screenshots

Location: `screenshots/`

Automatically captured when tests fail:
- Filename: `test_function_name.png`
- Useful for debugging failures
- Shows page state at moment of failure

### Test Reports

Reports can be generated using pytest plugins:

```bash
# Install HTML report plugin
pip install pytest-html

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### 1. **ChromeDriver Version Mismatch**

**Error:** `selenium.common.exceptions.SessionNotCreatedException`

**Solution:**
```bash
# The project uses webdriver-manager, which auto-downloads correct version
# If issue persists, clear cache:
pip install --upgrade webdriver-manager

# Or manually specify Chrome version
```

#### 2. **Element Not Found**

**Error:** `selenium.common.exceptions.NoSuchElementException`

**Causes:**
- Incorrect locator
- Element not loaded yet
- Page structure changed

**Solution:**
```python
# Ensure explicit wait is used
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))
```

#### 3. **Tests Timeout**

**Error:** `TimeoutException`

**Solution:**
- Increase wait time in WebDriverWait
- Check network/site performance
- Verify internet connection

#### 4. **Import Errors**

**Error:** `ModuleNotFoundError`

**Solution:**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate

# Reinstall requirements
pip install -r requirements.txt
```

#### 5. **Port Already in Use**

If running local server:
```bash
# Change port in configuration
# Or kill process using the port
```

#### 6. **Screenshot Directory Permission Error**

**Solution:**
```bash
# Ensure screenshots folder has write permissions
# Or delete old screenshots to free space
```

---

## 📝 Writing New Tests

### Template for New Test

```python
from pages.your_page import YourPage
from utils.logger import setup_logger
import time

logger = setup_logger()

def test_new_feature(driver):
    # Arrange - Navigate to page
    driver.get("https://practicesoftwaretesting.com/page")
    logger.info("Page Opened")
    
    # Act - Perform actions
    page = YourPage(driver)
    page.perform_action()
    logger.info("Action Performed")
    
    # Assert - Verify results
    assert page.verify_result() == True
    logger.info("Test Passed")
```

### Creating New Page Object

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewPage:
    # Locators
    ELEMENT_LOCATOR = (By.ID, "element_id")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def method_name(self):
        element = self.wait.until(EC.visibility_of_element_located(self.ELEMENT_LOCATOR))
        element.click()
        return True
```

---

## 🔗 Useful Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Python Official Documentation](https://docs.python.org/3/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

---

## 📞 Support & Contribution

For issues, questions, or contributions:

1. Check existing test cases for similar scenarios
2. Review logs and screenshots for debugging
3. Ensure all dependencies are installed
4. Run tests in verbose mode for detailed output

---

## 📄 License

This project is for educational and testing purposes.

---

## ✅ Checklist Before Running Tests

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Chrome browser installed
- [ ] Project structure intact
- [ ] No network/firewall restrictions
- [ ] Logs directory has write permissions

---

**Happy Testing! 🎉**

For detailed information about specific test cases, refer to individual test files in the `tests/` directory.
