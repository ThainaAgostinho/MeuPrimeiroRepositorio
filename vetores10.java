import java.util.Scanner;
import  java.util.ArrayList;
import  java.util.Collections ;
import  java.util.List ;
public class vetores10 {
    
        public static void main(String[] args)  {
        Scanner in = new Scanner (System.in);
        int [] valores = new int [28];
        List < Double > media = new ArrayList<>();
        double resultado; 
        double mediaMaior; 
        double mediaMenor;
    for (int i = 0; i<28; i++) { System.out.printf("digite o valor [%d]:", (i+1));
        valores [i] = in.nextInt ();}

    int somaElementos= 0;
    for (int x = 0; x<28; x++) { 
     somaElementos =+ valores[x];}

   //System.out.printf("A soma dos valores é h: %d\n", somaElementos );
  double soma = somaElementos;
  resultado  = (soma/4.0);
  media.add(resultado);
  System.out.printf("a média mensal foi " + (resultado));

mediaMaior = Collections.max(media);
mediaMenor = Collections.min(media);
System.out.printf("a maior média foi " + (mediaMaior));
System.out.printf("a menor média foi " + (mediaMenor));
    
        }
}