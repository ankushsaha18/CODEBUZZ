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

## Proctoring Functionality

The application includes proctoring functionality that uses computer vision libraries (MediaPipe and OpenCV) for face detection. These libraries are optional and only needed if you want to use the proctoring features.

If these libraries cannot be installed during deployment, the proctoring functionality will be automatically disabled, but the rest of the application will work normally.

## Troubleshooting

### Common Deployment Issues

1. **Package Installation Errors**: 
   - If you encounter issues with package installation, ensure you're using Python 3.9
   - The requirements.txt has been updated to make computer vision libraries optional

2. **Static Files Issues**:
   - Make sure `python manage.py collectstatic` has been run
   - Check that the STATIC_ROOT and STATIC_URL settings are correct in settings.py

3. **Database Migration Issues**:
   - Run `python manage.py migrate` to ensure all database migrations are applied
   - For PostgreSQL, ensure the DATABASE_URL environment variable is set correctly

4. **HackerEarth API Issues**:
   - Verify that the HE_CLIENT_SECRET environment variable is set
   - Check that your HackerEarth API key is valid and has not expired

5. **Computer Vision Library Issues**:
   - The proctoring feature uses MediaPipe and OpenCV for face detection
   - These libraries are optional and the application will work without them
   - If you want to enable proctoring, you may need to manually install these libraries
   - You can test the installation with: `python test_cv.py`

### Python Version Compatibility

This project is configured to use Python 3.9 to ensure compatibility with Render's deployment environment.

## Testing Computer Vision Libraries

To verify that the computer vision libraries (MediaPipe, OpenCV) are correctly installed and functional:

```bash
python test_cv.py
```

This script will test the imports and basic functionality of the required libraries. Note that these libraries are optional, and the application will work normally even if they are not available.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.