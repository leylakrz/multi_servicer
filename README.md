# FastAPI Project with Factory and Abstract Factory Patterns

This project is a simple FastAPI application that implements the factory and abstract factory design patterns. It was developed as part of a code challenge during an interview process.

## Code Challenge Description

The code challenge consisted of two tasks:

1. **Dynamic Provider Selection**: Implement a program that can choose a provider at runtime to execute commands such as sending SMS, MMS, and emails. The provider selection should be flexible and should allow commands to be executed on specific providers.
   
   Example:
   ```python
   Command(provider="google").run("MMS", phone_number)
   Command(provider="google").run("email", email)
   ```

2. **Automatic Provider Selection**: Implement the program in a way that it automatically selects the first available provider to execute the command. There should be a mechanism to clarify which provider is available at the time of execution.

   Example:
   ```python
   Command.run("MMS", phone_number)
   ```

## Project Structure

- **`_1.py`**: Contains the implementation for the first part of the code challenge, where providers are selected dynamically based on runtime parameters.
- **`_2.py`**: Contains the implementation for the second part of the code challenge, where the program automatically selects the first available provider.
- **`main.py`**: Includes the FastAPI application and routers for handling HTTP requests and responses.
- **`schemas.py`**: Includes schemas for request data validation, utilized by the FastAPI routers.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```


## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are highly appreciated!