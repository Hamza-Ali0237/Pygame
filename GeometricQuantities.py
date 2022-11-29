# importing math module for extracting the value of pi
import math

# Class of finding area of 2D Figures
class TwoDimensionFigures :
    Area = 0.0
    area = 0.00
    # Constructor
    def __init__(self) :
        print("_________________Calculating 2D Figures_________________")

    # Method for area of Scalene Triangle
    def ScaleneTriangleArea(self, b,  h) :
        self.area = 0.5 * b * h
        self.Area = "{:.2f}".format(self.area)
        return self.Area

    # Method for area of Isosceless Triangle
    def IsoscelessTriangleArea(self, b,  h) :
        self.area = 0.5 * b * h
        self.Area = "{:.2f}".format(self.area)
        return self.Area

    # Method for area of Equilateral Triangle
    def EquilateralTriangleArea(self, a) :
        self.area = (1.732 * a * a) / 4
        self.Area = "{:.2f}".format(self.area)
        return self.Area

    # Method for area of Right Angle Triangle
    def rightTriangleArea(self, a,  b) :
        self.area = 0.5 * b * a
        self.Area = "{:.2f}".format(self.area)
        return self.Area



# Class of finding area of 3D Solids
class ThreeDimensionalSolids:
    volume = 0.0
    Volume = 0.00

    # Constructor
    def __init__(self):
        print("_________________Calculating 3D Solids_________________")

    # Method for volume of a Triangular Pyramid
    def triangularPyramid(self, base, height):
        self.Volume = 1/3 * (base * height)
        self.volume = "{:.2f}".format(self.Volume)
        return self.volume

    # Method for volume of a Cube
    def cube(self, base):
        self.Volume = base**3
        self.volume = "{:.2f}".format(self.Volume)
        return self.volume

    # Method for volume of a Square Pyramid
    def squarePyramid(self, base, height):
        self.Volume = (base**2) * (height/3)
        self.volume = "{:.2f}".format(self.Volume)
        return self.volume

    # Method for volume of a Cone
    def cone(self, radius, height):
        self.Volume = math.pi * (radius**2) * (height/3)
        self.volume = "{:.2f}".format(self.Volume)
        return self.volume

    # Method for volume of a Cylinder
    def cylinder(self, radius, height):
        self.Volume = math.pi * (radius**2) * (height)
        self.volume = "{:.2f}".format(self.Volume)
        return str(self.volume)
    

# Class for converting different units
class MetricConversion():
    inches = 0.0
    meter = 0.0
    cm = 0.0
    feet = 0.0
    
    def __init__(self):
        pass
    
    def inchToFeet(self, inches):
        self.feet = inches / 12
        return self.feet
    
    def inchToCentimeter(self, inches):
        self.cm = 2.54 * inches
        return self.cm

    def inchToMeter(self, inches):
        self.meter = inches  * 0.0254
        return self.meter

    def feetToInch(self, feet):
        self.inches = feet * 12
        return self.inches

    def feetToCentimeter(self, feet):
        self.cm = 30.48 * feet
        return self.cm
    
    def feetToMeter(self, feet):
        self.meter = feet * 0.3048
        return self.meter

    def cmToInch(self, cm):
        self.inches = cm / 2.54
        return self.inches

    def cmToFeet(self, cm):
        self.feet = cm / 30.48
        return self.feet

    def cmToMeter(self, cm):
        self.meter = cm / 100
        return self.meter

    def meterToInch(self, meter):
        self.inches = meter / 0.0254
        return self.inches

    def meterToFeet(self, meter):
        self.feet = meter / 0.3048
        return self.feet

    def meterToCentimeter(self, meter):
        self.cm = meter * 100
        return self.cm

# Class for Main Method
class GeometricQuantities:

    # Making the method Static so it can work without an instance
    @staticmethod
    def main( args) :

        metricCon = MetricConversion()
        # For Welcome Screen
        print("---------------------Welcome ABC Company------------------------")
        # Name of Program and......Enter Your name of IDs here....................
        print("---------------------Name of IDs------------------------")
        # Option for the user to choose figures            
        print("Select an option \n1. 2D Figures\n2. 3D Figures")
        ch = int(input())
        
        
        #For Calculating 2D figures
        if ch == 1 :
            print("Choose Figure Name: \n1.Scalene\n2.Isosceless\n3.Equilateral\n4.Right\n")
            print("Enter Which Figure You Want")
            chooseFigure_1 = int(input()) 

            print("Choose which Metric or Imperial Unit do you want to input data in: \n1. Inches \n2. Feet \n3. Centimeters \n4. Meter \n")
            metricInput = int(input())

            print("\nChoose which Metric or Imperial Unit do you want for output: \n1. Inches \n2. Feet \n3. Centimeters \n4. Meter \n")
            metricOutput = int(input())
            
            t = TwoDimensionFigures()
            if chooseFigure_1 == 1 :
                    print("Enter Base")
                    b = int(input())
                    print("Enter Height")
                    h = int(input())
                    
                    if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.ScaleneTriangleArea(b, h)) + " Inches")
                    if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.ScaleneTriangleArea(b, h))) + " Feet")
                    if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.ScaleneTriangleArea(b, h))) + " cm")
                    if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.ScaleneTriangleArea(b, h))) + " meters")


                    if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.ScaleneTriangleArea(b, h))) + " Inch")
                    if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.ScaleneTriangleArea(b, h) + " Feet"))
                    if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.ScaleneTriangleArea(b, h))) + " cm")
                    if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.ScaleneTriangleArea(b, h))) + " meters")


                    if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.ScaleneTriangleArea(b, h))) + " Inch")
                    if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.ScaleneTriangleArea(b, h))) + " Feet")
                    if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.ScaleneTriangleArea(b, h) + " cm"))
                    if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.ScaleneTriangleArea(b, h))) + " meters")


                    if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.ScaleneTriangleArea(b, h))) + " Inch")
                    if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.ScaleneTriangleArea(b, h))) + " Feet")
                    if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.ScaleneTriangleArea(b, h))) + " cm")
                    if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.ScaleneTriangleArea(b, h) + " meters"))

                            

            if chooseFigure_1 == 2 :
                    print("Enter Base")
                    b = int(input())
                    print("Enter Height")
                    h = int(input())

                    if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.IsoscelessTriangleArea(b, h)) + " Inches")
                    if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.IsoscelessTriangleArea(b, h))) + " Feet")
                    if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.IsoscelessTriangleArea(b, h))) + " cm")
                    if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.IsoscelessTriangleArea(b, h))) + " meters")


                    if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.IsoscelessTriangleArea(b, h))) + " Inch")
                    if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.IsoscelessTriangleArea(b, h) + " Feet"))
                    if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.IsoscelessTriangleArea(b, h))) + " cm")
                    if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.IsoscelessTriangleArea(b, h))) + " meters")


                    if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.IsoscelessTriangleArea(b, h))) + " Inch")
                    if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.IsoscelessTriangleArea(b, h))) + " Feet")
                    if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.IsoscelessTriangleArea(b, h) + " cm"))
                    if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.IsoscelessTriangleArea(b, h))) + " meters")


                    if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.IsoscelessTriangleArea(b, h))) + " Inch")
                    if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.IsoscelessTriangleArea(b, h))) + " Feet")
                    if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.IsoscelessTriangleArea(b, h))) + " cm")
                    if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.IsoscelessTriangleArea(b, h) + " meters"))


            if chooseFigure_1 == 3 :
                    print("Enter Side")
                    b = int(input())

                    if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.EquilateralTriangleArea(b)) + " Inches")
                    if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.EquilateralTriangleArea(b))) + " Feet")
                    if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.EquilateralTriangleArea(b))) + " cm")
                    if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.EquilateralTriangleArea(b))) + " meters")


                    if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.EquilateralTriangleArea(b))) + " Inch")
                    if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.EquilateralTriangleArea(b) + " Feet"))
                    if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.EquilateralTriangleArea(b))) + " cm")
                    if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.EquilateralTriangleArea(b))) + " meters")


                    if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.EquilateralTriangleArea(b))) + " Inch")
                    if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.EquilateralTriangleArea(b))) + " Feet")
                    if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.EquilateralTriangleArea(b) + " cm"))
                    if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.EquilateralTriangleArea(b))) + " meters")


                    if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.EquilateralTriangleArea(b))) + " Inch")
                    if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.EquilateralTriangleArea(b))) + " Feet")
                    if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.EquilateralTriangleArea(b))) + " cm")
                    if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.EquilateralTriangleArea(b) + " meters"))

                    
            if chooseFigure_1 == 4 :
                    print("Enter Side1")
                    a = int(input())
                    print("Enter Side2")
                    b = int(input())
                    print("Enter Hyptenuese")
                    h = int(input())
                    l = a * a + b * b
                    if l == h :

                        if(metricInput == 1):
                            if(metricOutput == 1):
                                print(str(t.rightTriangleArea(a, b)) + " Inches")
                        if(metricInput == 1):
                            if(metricOutput == 2):
                                print(str(metricCon.inchToFeet(t.rightTriangleArea(a, b))) + " Feet")
                        if(metricInput == 1):
                            if(metricOutput == 3):
                                print(str(metricCon.inchToCentimeter(t.rightTriangleArea(a, b))) + " cm")
                        if(metricInput == 1):
                            if(metricOutput == 4):
                                print(str(metricCon.inchToMeter(t.rightTriangleArea(a, b))) + " meters")


                        if(metricInput == 2):
                            if(metricOutput == 1):
                                print(str(metricCon.feetToInch(t.rightTriangleArea(a, b))) + " Inch")
                        if(metricInput == 2):
                            if(metricOutput == 2):
                                print(str(t.rightTriangleArea(a, b) + " Feet"))
                        if(metricInput == 2):
                            if(metricOutput == 3):
                                print(str(metricCon.feetToCentimeter(t.rightTriangleArea(a, b))) + " cm")
                        if(metricInput == 2):
                            if(metricOutput == 4):
                                print(str(metricCon.feetToMeter(t.rightTriangleArea(a, b))) + " meters")


                        if(metricInput == 3):
                            if(metricOutput == 1):
                                print(str(metricCon.cmToInch(t.rightTriangleArea(a, b))) + " Inch")
                        if(metricInput == 3):
                            if(metricOutput == 2):
                                print(str(metricCon.cmToFeet(t.rightTriangleArea(a, b))) + " Feet")
                        if(metricInput == 3):
                            if(metricOutput == 3):
                                print(str(t.rightTriangleArea(a, b) + " cm"))
                        if(metricInput == 3):
                            if(metricOutput == 4):
                                print(str(metricCon.cmToMeter(t.rightTriangleArea(a, b))) + " meters")


                        if(metricInput == 4):
                            if(metricOutput == 1):
                                print(str(metricCon.meterToInch(t.rightTriangleArea(a, b))) + " Inch")
                        if(metricInput == 4):
                            if(metricOutput == 2):
                                print(str(metricCon.meterToFeet(t.rightTriangleArea(a, b))) + " Feet")
                        if(metricInput == 4):
                            if(metricOutput == 3):
                                print(str(metricCon.meterToCentimeter(t.rightTriangleArea(a, b))) + " cm")
                        if(metricInput == 4):
                            if(metricOutput == 4):
                                print(str(t.rightTriangleArea(a, b) + " meters"))
                    else:
                        print("It is not a Right Angle Triangle.\n")
            

        #For Calculating 3D solids
        if ch == 2 :
            print("Choose Figure Name: \n1.Triangular Pyramid\n2.Cube\n3.Square Pyramid\n4.Cone\n5.Cylinder\n")
            print("Enter The Solid you want to be calculated")
            chooseFigure = int(input())

            print("Choose which Metric or Imperial Unit do you want to input data in: \n1. Inches \n2. Feet \n3. Centimeters \n4. Meter \n")
            metricInput = int(input())

            print("\nChoose which Metric or Imperial Unit do you want for output: \n1. Inches \n2. Feet \n3. Centimeters \n4. Meter \n")
            metricOutput = int(input())
            
            t = ThreeDimensionalSolids()
            if chooseFigure == 1 :
                print("Enter Base")
                b = int(input())
                print("Enter Height")
                h = int(input())

                if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.triangularPyramid(b, h)) + " Inches")
                if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.triangularPyramid(b, h))) + " Feet")
                if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.triangularPyramid(b, h))) + " cm")
                if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.triangularPyramid(b, h))) + " meters")


                if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.triangularPyramid(b, h))) + " Inch")
                if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.triangularPyramid(b, h) + " Feet"))
                if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.triangularPyramid(b, h))) + " cm")
                if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.triangularPyramid(b, h))) + " meters")


                if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.triangularPyramid(b, h))) + " Inch")
                if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.triangularPyramid(b, h))) + " Feet")
                if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.triangularPyramid(b, h) + " cm"))
                if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.triangularPyramid(b, h))) + " meters")


                if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.triangularPyramid(b, h))) + " Inch")
                if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.triangularPyramid(b, h))) + " Feet")
                if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.triangularPyramid(b, h))) + " cm")
                if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.triangularPyramid(b, h) + " meters"))

                
            if chooseFigure == 2 :
                print("Enter Base")
                b = int(input())

                if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.cube(b)) + " Inches")
                if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.cube(b))) + " Feet")
                if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.cube(b))) + " cm")
                if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.cube(b))) + " meters")


                if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.cube(b))) + " Inch")
                if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.cube(b) + " Feet"))
                if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.cube(b))) + " cm")
                if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.cube(b))) + " meters")


                if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.cube(b))) + " Inch")
                if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.cube(b))) + " Feet")
                if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.cube(b) + " cm"))
                if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.cube(b))) + " meters")


                if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.cube(b))) + " Inch")
                if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.cube(b))) + " Feet")
                if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.cube(b))) + " cm")
                if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.cube(b) + " meters"))

                
            if chooseFigure == 3 :
                print("Enter Base")
                b = int(input())
                print("Enter Height")
                h = int(input())

                if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.squarePyramid(b, h)) + " Inches")
                if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.squarePyramid(b, h))) + " Feet")
                if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.squarePyramid(b, h))) + " cm")
                if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.squarePyramid(b, h))) + " meters")


                if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.squarePyramid(b, h))) + " Inch")
                if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.squarePyramid(b, h) + " Feet"))
                if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.squarePyramid(b, h))) + " cm")
                if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.squarePyramid(b, h))) + " meters")


                if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.squarePyramid(b, h))) + " Inch")
                if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.squarePyramid(b, h))) + " Feet")
                if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.squarePyramid(b, h) + " cm"))
                if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.squarePyramid(b, h))) + " meters")


                if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.squarePyramid(b, h))) + " Inch")
                if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.squarePyramid(b, h))) + " Feet")
                if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.squarePyramid(b, h))) + " cm")
                if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.squarePyramid(b, h) + " meters"))

                
            
            if chooseFigure == 5 :
                print("Enter Radius")
                r = int(input())
                print("Enter Height")
                h = int(input())

                if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.cylinder(r ,h)) + " Inches")
                if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.cylinder(r ,h))) + " Feet")
                if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.cylinder(r ,h))) + " cm")
                if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.cylinder(r ,h))) + " meters")


                if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.cylinder(r ,h))) + " Inch")
                if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.cylinder(r ,h) + " Feet"))
                if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.cylinder(r ,h))) + " cm")
                if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.cylinder(r ,h))) + " meters")


                if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.cylinder(r ,h))) + " Inch")
                if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.cylinder(r ,h))) + " Feet")
                if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.cube(b) + " cm"))
                if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.cylinder(r ,h))) + " meters")


                if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.cylinder(r ,h))) + " Inch")
                if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.cylinder(r ,h))) + " Feet")
                if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.cylinder(r ,h))) + " cm")
                if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.cylinder() + " meters"))

                
            if chooseFigure == 4:
                print("Enter Base")
                b = int(input())
                print("Enter Height")
                h = int(input())

                if(metricInput == 1):
                        if(metricOutput == 1):
                            print(str(t.cone(r, h)) + " Inches")
                if(metricInput == 1):
                        if(metricOutput == 2):
                            print(str(metricCon.inchToFeet(t.cone(r, h))) + " Feet")
                if(metricInput == 1):
                        if(metricOutput == 3):
                            print(str(metricCon.inchToCentimeter(t.cone(r, h))) + " cm")
                if(metricInput == 1):
                        if(metricOutput == 4):
                            print(str(metricCon.inchToMeter(t.cone(r, h))) + " meters")


                if(metricInput == 2):
                        if(metricOutput == 1):
                            print(str(metricCon.feetToInch(t.cone(r, h))) + " Inch")
                if(metricInput == 2):
                        if(metricOutput == 2):
                            print(str(t.cone(r, h) + " Feet"))
                if(metricInput == 2):
                        if(metricOutput == 3):
                            print(str(metricCon.feetToCentimeter(t.cone(r, h))) + " cm")
                if(metricInput == 2):
                        if(metricOutput == 4):
                            print(str(metricCon.feetToMeter(t.cone(r, h))) + " meters")


                if(metricInput == 3):
                        if(metricOutput == 1):
                            print(str(metricCon.cmToInch(t.cone(r, h))) + " Inch")
                if(metricInput == 3):
                        if(metricOutput == 2):
                            print(str(metricCon.cmToFeet(t.cone(r, h))) + " Feet")
                if(metricInput == 3):
                        if(metricOutput == 3):
                            print(str(t.cone(r, h) + " cm"))
                if(metricInput == 3):
                        if(metricOutput == 4):
                            print(str(metricCon.cmToMeter(t.cone(r, h))) + " meters")


                if(metricInput == 4):
                        if(metricOutput == 1):
                            print(str(metricCon.meterToInch(t.cone(r, h))) + " Inch")
                if(metricInput == 4):
                        if(metricOutput == 2):
                            print(str(metricCon.meterToFeet(t.cone(r, h))) + " Feet")
                if(metricInput == 4):
                        if(metricOutput == 3):
                            print(str(metricCon.meterToCentimeter(t.cone(r, h))) + " cm")
                if(metricInput == 4):
                        if(metricOutput == 4):
                            print(str(t.cone(r, h) + " meters"))

                

if __name__=="__main__":
    GeometricQuantities.main([])