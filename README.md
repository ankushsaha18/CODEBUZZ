# CODEBUZZ (hackIDE)

An online code editor, compiler, and interpreter built using Django and powered by the HackerEarth API.

## Features

- Online code editing with syntax highlighting
- Code execution using HackerEarth API
- Save code to the cloud
- Download code as a zipped file
- User profiles to store personal code and settings (in progress)

## Prerequisites

- Python 3.9+
- pip
- A HackerEarth API key

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CODEBUZZ-master
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your HackerEarth API key as an environment variable:
   ```bash
   export HE_CLIENT_SECRET=your_hackerearth_api_key
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment to Render

This application is configured for deployment to Render using the provided `render.yaml` configuration file.

### Environment Variables

Set the following environment variables in your Render dashboard:

- `SECRET_KEY` - Django secret key (generate a secure one)
- `DEBUG` - Set to "False" for production
- `HE_CLIENT_SECRET` - Your HackerEarth API key
- `DATABASE_URL` - PostgreSQL database URL (if using PostgreSQL)

### Deployment Steps

1. Fork this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set the environment variables mentioned above
5. Deploy!

The build process will automatically:
- Install dependencies from requirements.txt
- Collect static files
- Run database migrations

## Configuration

### HackerEarth API

To use the code execution feature, you need a HackerEarth API key:
1. Sign up at https://www.hackerearth.com/
2. Get your API key from the dashboard
3. Set it as the `HE_CLIENT_SECRET` environment variable

### Database

The application uses SQLite by default for development. For production deployment on Render, it will use PostgreSQL if a `DATABASE_URL` environment variable is provided.

## Troubleshooting

- If you encounter issues with static files, ensure `python manage.py collectstatic` has been run
- For database issues, make sure you've run `python manage.py migrate`
- Check Render logs for deployment errors

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.