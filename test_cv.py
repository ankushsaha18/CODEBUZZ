#!/usr/bin/env python
"""
Test script to verify computer vision libraries installation and basic functionality
"""

def test_opencv():
    try:
        import cv2
        print(f"OpenCV version: {cv2.__version__}")
        print("OpenCV import successful")
        return True
    except ImportError as e:
        print(f"OpenCV import failed: {e}")
        print("OpenCV is optional and only needed for proctoring functionality")
        return False

def test_mediapipe():
    try:
        import mediapipe as mp
        print(f"MediaPipe version: {mp.__version__}")
        print("MediaPipe import successful")
        return True
    except ImportError as e:
        print(f"MediaPipe import failed: {e}")
        print("MediaPipe is optional and only needed for proctoring functionality")
        return False

def test_numpy():
    try:
        import numpy as np
        print(f"NumPy version: {np.__version__}")
        print("NumPy import successful")
        return True
    except ImportError as e:
        print(f"NumPy import failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing computer vision library imports...")
    print("=" * 50)
    
    success = True
    success &= test_numpy()
    opencv_available = test_opencv()
    mediapipe_available = test_mediapipe()
    
    print("=" * 50)
    if success and (opencv_available and mediapipe_available):
        print("All tests passed! Computer vision libraries are ready.")
    elif success:
        print("Core libraries are ready. Computer vision libraries are optional.")
        print("Proctoring functionality will be disabled if computer vision libraries are not available.")
    else:
        print("Some tests failed. Please check the installation.")