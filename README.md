# Euclidean Distance Calculator

This project is created for the IBM CyberStart Program.

It is a simple Python program that calculates the Euclidean distance between pairs of points in a 2D space and finds the minimum distance among them.

## Overview

The Euclidean distance is the "ordinary" straight-line distance between two points in Euclidean space. This program allows you to define a list of points, calculate the distances between each pair of points, and determine the minimum distance.

## Features

- Define points in a 2D space.
- Calculate the Euclidean distance between each pair of points.
- Find and display the minimum Euclidean distance.

## Code Explanation

### Euclidean Distance Function

The `euclideanDistance` function calculates the Euclidean distance between two points `(x1, y1)` and `(x2, y2)`:

```python
import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
