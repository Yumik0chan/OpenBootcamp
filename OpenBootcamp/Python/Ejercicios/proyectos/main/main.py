import operaciones.division.division as d
import operaciones.multiplicacion.multiplicacion as m
import operaciones.resta.res as r
import operaciones.suma.sum as s


def main():
  divi = d.division(10 , 5)
  print(divi)
  multi = m.multiplicacion(7, 8)
  print(multi)
  resta = r.resta(7, 6)
  print(resta)
  suma = s.suma(15, 8)
  print(suma)

if __name__ == "__main__" :
    main()