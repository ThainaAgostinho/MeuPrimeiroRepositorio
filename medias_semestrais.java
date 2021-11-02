import java.util.Scanner;
import  java.util.ArrayList ;
import  java.util.List ;
import  java.text.DecimalFormat ;
import  java.util.Collections ;
import java.util.Formatter;

public class App { 
    public static void main(String[] args)  {

 List < Double > mediaAlunos = new ArrayList<>();
 List < String > resultadoAlunos = new ArrayList<>();

//Variáveis 
int alunosAprovados = 0, alunosReprovados = 0, alunosAF = 0 ;

Scanner sc = new Scanner (System.in);
DecimalFormat format = new DecimalFormat("0.0");

Double notaProva, notaProjeto, notaLista, resultado, mediaMaior, mediaMenor;
System.out.println("Olá, qual o seu nome?");
String user = sc.nextLine();
System.out.println("Qual  a quantidade de alunos na turma?");
int totalAlunos = sc. nextInt ();
for (int i = 1; i <= totalAlunos; i++)
 {System.out.println("Digite a nota da prova do aluno:");
      notaProva = sc. nextDouble();
System.out.println("Digite a nota do Projeto do aluno:");
      notaProjeto = sc.nextDouble();
 System.out.println("Digite a nota da Lista de Exercícios do aluno:");
      notaLista = sc.nextDouble();

      resultado = (notaProva + notaProjeto + notaLista)/3;
      mediaAlunos.add (resultado);

      if ( resultado< 5) {System.out.println("Resultado: Reprovado");
     resultadoAlunos.add ("Reprovado");
     alunosReprovados += 1;

    }  else if (resultado <= 7.9) {System.out.println("Resultado: Avaliação Final");
     resultadoAlunos.add ("Avaliação final");
     alunosAF += 1;

    }else {System.out.println("Resultado: Aprovado");
    resultadoAlunos.add ("Aprovado");
    alunosAprovados += 1;} }
mediaMaior = Collections.max(mediaAlunos);
mediaMenor = Collections.min(mediaAlunos);
System.out.println(" A maior média da turma foi: " +  (mediaMaior));
System.out.println(" A menor média da turma foi: " + (mediaMenor));

double mediaTurma;
 double mediaSoma = 0;
 //double notasFinais;

for (double notasFinais   : mediaAlunos) { mediaSoma += notasFinais;}
mediaTurma = mediaSoma / totalAlunos;
System.out.println(" A média de notas da turma foi: " + (mediaTurma));
System.out.println(" A quantidade de alunos aprovados foi: " + (alunosAprovados));
System.out.println(" A quantidade de alunos Reprovados foi: " + (alunosReprovados));
System.out.println(" A quantidade de alunos que precisa fazer a avaliação final é: " + (alunosAF));

sc.close();
   
}
}


