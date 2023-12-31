import pandas as pd
import numpy as np
from math import *

class Secante:
    def Secante(f, a, b, tol, niter):
        solucion = 0
        resultados = []
        x = a
        fa = eval(f)
        x = b
        fb = eval(f)
        Error = 100
        c = 0
        if a > b:
            mensaje = 'El intervalo es inadecuado'
            return None, mensaje, None
        elif fa == 0:
            solucion = a
            mensaje = f'{solucion} es raiz de f(x)'
            return None, mensaje, solucion
        elif fb == 0:
            solucion = b
            mensaje = f'{solucion} es raiz de f(x)'
            return None, mensaje, solucion
        elif fa*fb < 0:
            resultados.append([1,"{:.5f}".format(a),"{:.3e}".format(fa),100])
            resultados.append([2,"{:.5f}".format(b),"{:.3e}".format(fb),100])
            while Error > tol and c < niter:
                x = a - fa * (b - a) / (fb - fa)
                fx = eval(f)
                c = c + 1
                Error = abs(x - b)

                resultados.append([c+2,"{:.5f}".format(x),"{:.3e}".format(fx),"{:.3e}".format(Error)])

                a = b
                fa = fb
                b = x
                fb = fx

            if fx == 0:
                solucion = "{:.5f}".format(x)
                mensaje = str(solucion) + " es raiz de f(x)"
                return resultados, mensaje, solucion
            elif Error <= tol:
                solucion = "{:.5f}".format(x)
                mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
                return resultados, mensaje, solucion
            else:
                solucion = "{:.5f}".format(x)
                mensaje = "Fracaso en " + str(niter) + " iteraciones"
                return resultados, mensaje, None
        else:
            mensaje = "El intervalo es inadecuado"
            return None, mensaje, None
        
        
    def SecanteRel(f, a, b, tol, niter):
        solucion = 0
        resultados = []
        x = a
        fa = eval(f)
        x = b
        fb = eval(f)
        Error = 100
        c = 0
        if a > b:
            mensaje = 'El intervalo es inadecuado'
            return None, mensaje, None
        elif fa == 0:
            solucion = a
            mensaje = f'{solucion} es raiz de f(x)'
            return None, mensaje, solucion
        elif fb == 0:
            solucion = b
            mensaje = f'{solucion} es raiz de f(x)'
            return None, mensaje, solucion
        elif fa*fb < 0:
            resultados.append([1,"{:.5f}".format(a),"{:.3e}".format(fa),100])
            resultados.append([2,"{:.5f}".format(b),"{:.3e}".format(fb),100])
            while Error > tol and c < niter:
                x = a - fa * (b - a) / (fb - fa)
                fx = eval(f)
                c = c + 1
                Error = abs((x - b)/x)

                resultados.append([c+2,"{:.5f}".format(x),"{:.3e}".format(fx),"{:.3e}".format(Error)])

                a = b
                fa = fb
                b = x
                fb = fx

            if fx == 0:
                solucion = "{:.5f}".format(x)
                mensaje = str(solucion) + " es raiz de f(x)"
                return resultados, mensaje, solucion
            elif Error <= tol:
                solucion = "{:.5f}".format(x)
                mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
                return resultados, mensaje, solucion
            else:
                solucion = "{:.5f}".format(x)
                mensaje = "Fracaso en " + str(niter) + " iteraciones"
                return resultados, mensaje, None
        else:
            mensaje = "El intervalo es inadecuado"
            return None, mensaje, None  

#secante("x**3-x-1",1,2,0.5e-5,100)