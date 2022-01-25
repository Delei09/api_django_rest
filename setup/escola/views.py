from rest_framework import viewsets , generics
from escola.models import Aluno , Curso , Matricula
from escola.serializer import AlunoSerializer ,CursoSerializer , MatriculaSerializer , ListaMatriculasAlunoSerializer ,ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet) :
    # """" EXIBINDO TODOS OS ALUNOS """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet) :
    # """" EXIBINDO TODOS OS CURSOS """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet) :
    # """" EXIBINDO TODOS AS MATRICULAS """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView) :
    """" EXIBINDO MATRICULAS DE ALUNO E ALUNO """
    def get_queryset(self) :
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView) :
    """"LISTANDO ALUNSO MATRICULADOS"""
    def get_queryset(self) :
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer