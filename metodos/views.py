from django.shortcuts import render
from urllib.parse import quote, unquote
from metodos.Biseccion import Biseccion
from metodos.Grafica import Grafica
from metodos.InputFixed import InputFixed
from metodos.Newton import NewtonRaphson
from metodos.Secante import Secante
from metodos.PuntoFijo import PuntoFijo
from metodos.ReglaFalsa import ReglaFalsa
from metodos.RaicesMultiples import RaicesMultiples
from metodos.RaicesMultiples2 import RaicesMultiples2
from metodos.polinomio import Polinomio
import matlab.engine
import numpy as np

eng = matlab.engine.start_matlab()

def index(request):
    grafica = None
    if request.method == 'POST':
        grafica = None
        funcion = request.POST['Funcion']
        Fcorregida = InputFixed.CorregirFuncion(funcion) 
        grafica = Grafica.Graficar(Fcorregida)
    return render(request, 'home.html', {'grafica': grafica})

def metodos(request):
    return render(request, 'metodos.html', {})

def reglafalsa(request):
    resultado = []
    mensaje = ""
    solucion = None
    grafica = None
    if request.method == 'POST':
        funcion = request.POST['Funcion']
        a = request.POST['LimiteInferior']
        b = request.POST['LimiteSuperior']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        a = float(a)
        b = float(b)
        tol = float(tol)
        niter = int(niter)

        if(error == 1):
            resultado, mensaje, solucion = ReglaFalsa.ReglaFalsa(funcion, a, b, tol, niter)
        else:
            resultado, mensaje, solucion = ReglaFalsa.ReglaFalsaRel(funcion, a, b, tol, niter)

        if(solucion == None):
            pass
        else:
            grafica = Grafica.GraficarSolucion(funcion, float(solucion))

    return render(request, 'reglafalsa.html', {'resultado': resultado, 'mensaje': mensaje, 'solucion': solucion, 'grafica': grafica})

def newtonRaphson(request):
    resultado = []
    mensaje = ""
    grafica = None
    if request.method == 'POST':
        funcion = request.POST['Funcion']
        funcionDerivada = request.POST['primeraDerivada']
        x0 = request.POST['valorInicial']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        x0 = float(x0)
        tol = float(tol)
        niter = int(niter)
        if(error == 1):
            resultado, mensaje, solucion = NewtonRaphson.Newton(funcion,funcionDerivada, x0, tol, niter)
        else:
            resultado, mensaje, solucion = NewtonRaphson.NewtonRel(funcion,funcionDerivada, x0, tol, niter)

        if(solucion == None):
            pass
        else:
            grafica = Grafica.GraficarSolucion(funcion, float(solucion))
    return render(request, 'newtonRaphson.html',{'resultado': resultado, 'mensaje': mensaje, 'grafica': grafica})

def secante(request):
    resultado = []
    mensaje = ""
    grafica = None
    if request.method == 'POST':
        f = request.POST['Funcion']
        a = request.POST['inicialx0']
        b = request.POST['inicialx1']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        a = float(a)
        b = float(b)
        tol = float(tol)
        niter = int(niter)
        Fcorregida = InputFixed.CorregirFuncion(f)
        if(error == 1):
            resultado, mensaje, solucion = Secante.Secante(Fcorregida,a,b,tol,niter)
        else:
            resultado, mensaje, solucion = Secante.SecanteRel(Fcorregida,a,b,tol,niter)

        if(solucion == None):
            pass
        else:
            grafica = Grafica.GraficarSolucion(f, float(solucion))
    return render(request, 'secante.html',{'resultado': resultado, 'mensaje': mensaje, 'grafica': grafica})

def raicesMultiples(request):
    resultado = []
    mensaje = ""
    grafica = None
    if request.method == 'POST':
        Funcion = request.POST['Funcion']
        PrimeraDerivada = request.POST['PrimeraDerivada']
        SegundaDerivada = request.POST['SegundaDerivada']
        x0 = request.POST['ValorInicial']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        x0 = float(x0)
        tol = float(tol)
        niter = int(niter)
        if(error == 1):
            resultado, mensaje, solucion = RaicesMultiples.RaicesMultiples(Funcion ,PrimeraDerivada ,SegundaDerivada , x0, tol, niter)
        else:
            resultado, mensaje, solucion = RaicesMultiples.RaicesMultiplesRel(Funcion ,PrimeraDerivada ,SegundaDerivada , x0, tol, niter)

        if resultado == None:
            pass
        else:
            grafica = Grafica.GraficarSolucion(Funcion, float(solucion))
    return render(request, 'raicesmultiples.html',{'resultado': resultado, 'mensaje': mensaje, 'grafica': grafica})

def raicesMultiples2(request):
    resultado = []
    mensaje = ""
    grafica = None
    if request.method == 'POST':
        Funcion = request.POST['Funcion']
        PrimeraDerivada = request.POST['PrimeraDerivada']
        valorm = request.POST['m']
        x0 = request.POST['ValorInicial']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        valorm = int(valorm)
        error = int(error)
        x0 = float(x0)
        tol = float(tol)
        niter = int(niter)
        if(error == 1):
            resultado, mensaje, solucion = RaicesMultiples.RaicesMultiples(Funcion ,PrimeraDerivada ,valorm , x0, tol, niter)
        else:
            resultado, mensaje, solucion = RaicesMultiples.RaicesMultiplesRel(Funcion ,PrimeraDerivada ,valorm , x0, tol, niter)

        if resultado == None:
            pass
        else:
            grafica = Grafica.GraficarSolucion(Funcion, float(solucion))
    return render(request, 'raicesmultiples2.html',{'resultado': resultado, 'mensaje': mensaje, 'grafica': grafica})


def puntofijo(request):
    resultado = []
    mensaje = ""
    grafica = None
    if request.method == 'POST':
        Funcionf = request.POST['Funcionf']
        Funciong = request.POST['Funciong']
        x0 = request.POST['ValorInicial']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        x0 = float(x0)
        tol = float(tol)
        niter = int(niter)
        if(error == 1):
            resultado, mensaje, solucion = PuntoFijo.PuntoFijo(Funcionf,Funciong, x0, tol, niter)
        else:
             resultado, mensaje, solucion = PuntoFijo.PuntoFijoRel(Funcionf,Funciong, x0, tol, niter)
        
        if solucion == None:
            pass
        else:
            grafica = Grafica.GraficarSolucion(Funcionf,float(solucion))
    return render(request, 'puntofijo.html',{'resultado': resultado, 'mensaje': mensaje, 'grafica': grafica})

def biseccion(request):
    resultado = []
    mensaje = ""
    grafica = None
    if request.method == 'POST':
        funcion = request.POST['Funcion']
        limiteInf = request.POST['LimiteInferior']
        limiteSup = request.POST['LimiteSuperior']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        limiteInf = float(limiteInf)
        limiteSup = float(limiteSup)
        tol = float(tol)
        niter = int(niter)
        Fcorregida = InputFixed.CorregirFuncion(funcion)
        if(error == 1):
            resultado, mensaje, solucion = Biseccion.biseccion(Fcorregida, limiteInf, limiteSup, tol, niter)
        else:
            resultado, mensaje, solucion = Biseccion.biseccionRel(Fcorregida, limiteInf, limiteSup, tol, niter)

        if(solucion == None):
            pass
        else:
            grafica = Grafica.GraficarSolucion(funcion, float(solucion))
    return render(request, 'biseccion.html', {'resultado': resultado, 'mensaje': mensaje, 'grafica': grafica})

def jacobiSeid(request):
    datos_iteraciones = None
    mensaje = ""
    converge = ""

    if request.method == 'POST':
        filas = request.POST['rows']
        columnas = request.POST['columns']
        filas = int(filas)
        columnas = int(columnas)
        matrizA = [[0 for _ in range(columnas)] for _ in range(filas)]
        vectorB = [[0 for _ in range(1)]for _ in range(filas)]
        vectorX0 = [[0 for _ in range(1)]for _ in range(filas)]
        indice = 1
        for i in range(0, filas):
            for j in range(0, columnas):
                elemento = f'element_{indice}'
                matrizA[i][j] = float(request.POST[elemento])
                indice += 1
        indice = 1
        for i in range(0, filas):
            answer = f'answer_{indice}'
            vectorB[i][0] = float(request.POST[answer])
            indice += 1
        indice = 1
        for i in range(0, filas):
            initial = f'initial_{indice}'
            vectorX0[i][0] = float(request.POST[initial])
            indice += 1
        A = matlab.double(matrizA)
        b = matlab.double(vectorB)
        x0 = matlab.double(vectorX0)
        tol = request.POST['Tol']
        tol = float(tol)
        iteraciones = request.POST['Iter']
        iteraciones = int(iteraciones)
        met = request.POST['met']
        met = int(met)
        tipoError = request.POST['Error']
        if tipoError == 1:
            resultados = eng.MatJacobiSeid(x0,A,b,tol,iteraciones,met,nargout = 5)
        else:
            resultados = eng.MatJacobiSeidRel(x0,A,b,tol,iteraciones,met,nargout = 5)
        E = resultados[0]
        S = resultados[1]
        Iteraciones = resultados[2]
        x_values = np.array(Iteraciones)
        x_values = x_values.T
        valoresX = x_values.tolist()
        radioEspectral = resultados[4]
        solucion = resultados[3]

        for i in range(len(valoresX)):
            for j in range(len(valoresX[i])):
                valoresX[i][j] = "{:.5f}".format(valoresX[i][j])
                
        Error = np.array(E)
        for i in range(len(Error[0])):
            Error[0][i] = "{:.3e}".format(Error[0][i])
            
        datos_iteraciones = list(zip(valoresX, Error[0]))
        mensaje = str(S) + ' ' +  str(solucion)
        converge = solucion[0]
        if converge == 'E':
            converge = 'El metodo converge con un ρ(T) de ' + str(radioEspectral)
        else:
            converge = 'El metodo no converge porque su ρ(T) es de ' + str(radioEspectral)
        
        
    return render(request, 'jacobiSeid.html', {'datos_iteraciones': datos_iteraciones, 'mensaje':mensaje, 'converge':converge})


def SOR(request):
    datos_iteraciones = None
    mensaje = ''
    converge = ''
    if request.method == 'POST':
        filas = request.POST['rows']
        columnas = request.POST['columns']
        filas = int(filas)
        columnas = int(columnas)
        matrizA = [[0 for _ in range(columnas)] for _ in range(filas)]
        vectorB = [[0 for _ in range(1)]for _ in range(filas)]
        vectorX0 = [[0 for _ in range(1)]for _ in range(filas)]
        indice = 1
        for i in range(0, filas):
            for j in range(0, columnas):
                elemento = f'element_{indice}'
                matrizA[i][j] = float(request.POST[elemento])
                indice += 1
        indice = 1
        for i in range(0, filas):
            answer = f'answer_{indice}'
            vectorB[i][0] = float(request.POST[answer])
            indice += 1
        indice = 1
        for i in range(0, filas):
            initial = f'initial_{indice}'
            vectorX0[i][0] = float(request.POST[initial])
            indice += 1
        A = matlab.double(matrizA)
        b = matlab.double(vectorB)
        x0 = matlab.double(vectorX0)
        tol = request.POST['Tol']
        tol = float(tol)
        iteraciones = request.POST['Iter']
        iteraciones = int(iteraciones)
        valorW = request.POST['w']
        valorW = float(valorW)
        tipoError = request.POST['Error']
        if tipoError == 1:
            resultados = eng.SOR(x0, A, b, tol, iteraciones, valorW,nargout = 5)
        else:
            resultados = eng.SORrel(x0, A, b, tol, iteraciones, valorW,nargout = 5)
        E = resultados[0]
        S = resultados[1]
        Iteraciones = resultados[2]
        x_values = np.array(Iteraciones)
        x_values = x_values.T
        valoresX = x_values.tolist()
        radioEspectral = resultados[4]
        solucion = resultados [3]

        for i in range(len(valoresX)):
            for j in range(len(valoresX[i])):
                valoresX[i][j] = "{:.5f}".format(valoresX[i][j])

        Error = np.array(E)
        for i in range(len(Error[0])):
            Error[0][i] = "{:.3e}".format(Error[0][i])

        datos_iteraciones = list(zip(valoresX, Error[0]))
        mensaje = str(S) + ' ' +  str(solucion)
        converge = solucion[0]
        if converge == 'E':
            converge = 'El metodo converge con un ρ(T) de ' + str(radioEspectral)
        else:
            converge = 'El metodo no converge porque su ρ(T) es de ' + str(radioEspectral)
    return render(request, 'SOR.html', {'datos_iteraciones': datos_iteraciones, 'mensaje':mensaje, 'converge':converge})


def vandermonde(request):
    grafica = None
    if request.method == 'POST':
        columnas = request.POST['columns']
        columnas = int(columnas)
        vectorX = [[] for _ in range(columnas)]
        vectorY = [[] for _ in range(columnas)]
       
        for j in range(0, columnas):
                elemento = f'x_{j}'
                vectorX[j].append(float(request.POST[elemento]))
                
              
        for j in range(0, columnas):
                elemento = f'y_{j}'
                vectorY[j].append(float(request.POST[elemento]))
        x = matlab.double(vectorX)
        y = matlab.double(vectorY)
        Result = eng.vander(x,y)

        grado = len(Result[0])
        coeficientes = [item[0] for item in Result]
        print(coeficientes)
        # Crear el polinomio a partir de los coeficientes
        polinomiores = Polinomio.crear_polinomio_vander(coeficientes)

        x_np = np.array(x)
        minimo_x = np.min(x_np)
        maximo_x = np.max(x_np)

        y_np = np.array(y)
        minimo_y = np.min(y_np)
        maximo_y = np.max(y_np)


        grafica = Grafica.GraficarPolinomio(polinomiores,minimo_x,maximo_x,minimo_y,maximo_y)

        # Imprimir el polinomio
       

        
    return render(request, 'vandermonde.html',  {'grafica': grafica})

def newton(request):
    grafica = None
    if request.method == 'POST':
        columnas = request.POST['columns']
        columnas = int(columnas)
        vectorX = [[] for _ in range(columnas)]
        vectorY = [[] for _ in range(columnas)]
       
        for j in range(0, columnas):
                elemento = f'x_{j}'
                vectorX[j].append(float(request.POST[elemento]))
                
              
        for j in range(0, columnas):
                elemento = f'y_{j}'
                vectorY[j].append(float(request.POST[elemento]))
                
        x = matlab.double(vectorX)
        y = matlab.double(vectorY)

        x_np = np.array(x)
        x_np = x_np.flatten()
        minimo_x = np.min(x_np)
        maximo_x = np.max(x_np)

        y_np = np.array(y)
        y_np = y_np.flatten()
        minimo_y = np.min(y_np)
        maximo_y = np.max(y_np)

        Result = eng.Newtonint(x,y,nargout=2)

        tabla = np.array(Result[0])
        coef = np.array(Result[1])
        coef = coef.flatten()

        polinomiores = Polinomio.polinomio_newton_string(coef, x_np)
        


        grafica = Grafica.GraficarPolinomio(polinomiores,minimo_x,maximo_x,minimo_y,maximo_y)

        
       

        
    return render(request, 'newton.html',  {'grafica': grafica})

def lagrange(request):
    grafica = None
    if request.method == 'POST':
        columnas = request.POST['columns']
        columnas = int(columnas)
        vectorX = [[] for _ in range(columnas)]
        vectorY = [[] for _ in range(columnas)]
       
        for j in range(0, columnas):
                elemento = f'x_{j}'
                vectorX[j].append(float(request.POST[elemento]))
                
              
        for j in range(0, columnas):
                elemento = f'y_{j}'
                vectorY[j].append(float(request.POST[elemento]))
                
                
        x = matlab.double(vectorX)
        y = matlab.double(vectorY)
        
        x_np = np.array(x)
        x_np_np = x_np.flatten()
        minimo_x = np.min(x_np)
        maximo_x = np.max(x_np)

        y_np = np.array(y)
        y_np = y_np.flatten()
        minimo_y = np.min(y_np)
        maximo_y = np.max(y_np)

        Result = eng.Lagrange(x,y)
        

        polinomiores = Polinomio.lagrange_polynomial(x_np, y_np)
        

        grafica = Grafica.GraficarPolinomio(polinomiores,minimo_x,maximo_x,minimo_y,maximo_y)
       
       

        
    return render(request, 'lagrange.html',  {'grafica': grafica})

def spline(request):
    grafica = None
    if request.method == 'POST':
        columnas = request.POST['columns']
        columnas = int(columnas)
        vectorX = [[] for _ in range(columnas)]
        vectorY = [[] for _ in range(columnas)]
       
        for j in range(0, columnas):
                elemento = f'x_{j}'
                vectorX[j].append(float(request.POST[elemento]))
                
              
        for j in range(0, columnas):
                elemento = f'y_{j}'
                vectorY[j].append(float(request.POST[elemento]))
                
                
        x = matlab.double(vectorX)
        y = matlab.double(vectorY)
        d = 3

        x_np = np.array(x)
        x_np_np = x_np.flatten()
        minimo_x = np.min(x_np)
        maximo_x = np.max(x_np)

        y_np = np.array(y)
        y_np = y_np.flatten()
        minimo_y = np.min(y_np)
        maximo_y = np.max(y_np)

        Result = eng.Spline(x,y,d)
        Result_np = np.array(Result)
        funciones = []
        for i in range(len(x_np)-1):
            funcion = Polinomio.crear_polinomio_spline(Result[i])
            funciones.append(funcion)
       
        grafica = Grafica.GraficarFunciones(funciones,minimo_x,maximo_x,minimo_y,maximo_y)
       
       

        
    return render(request, 'spline.html',  {'grafica': grafica})