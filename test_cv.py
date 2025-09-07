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
        return False

def test_mediapipe():
    try:
        import mediapipe as mp
        print(f"MediaPipe version: {mp.__version__}")
        print("MediaPipe import successful")
        return True
    except ImportError as e:
        print(f"MediaPipe import failed: {e}")
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
    success &= test_opencv()
    success &= test_mediapipe()
    
    print("=" * 50)
    if success:
        print("All tests passed! Computer vision libraries are ready.")
    else:
        print("Some tests failed. Please check the installation.")