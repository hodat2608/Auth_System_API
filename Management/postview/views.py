from django.shortcuts import render
from rest_framework.response import Response
from postview.serializers import NoteSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from postview.models import Note_User
from django.contrib.auth import update_session_auth_hash
from rest_framework.permissions import IsAdminUser
from accounts.models import UserAccount
from postview.permission import ModifyNotePermission
class AdminViews(viewsets.ViewSet):

    permission_classes = [IsAuthenticated,IsAdminUser]
    def get_object(self,pk):
        try: 
            return  Note_User.objects.get(pk=pk) 
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'])
    def get_all_note(self,request,format=None):
        notes = Note_User.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add_note(self,request,format=None):
        data = request.data
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def get_detail_note(self,request,pk,format=None):
        note = self.get_object(pk) 
        serializer = NoteSerializer(note,many=False)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'])
    def modify_note(self,request,pk,format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    @action(detail=False, methods=['delete'])
    def delete_note(self,request,pk,format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserViews(viewsets.ViewSet):
    
    def get_user(self,request):
        try: 
            return UserAccount.objects.get(pk=request.user.id)
        except UserAccount.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)
        
    permission_classes =[IsAuthenticated,ModifyNotePermission]
    @action(detail=False, methods=['get'])
    def get_notes(self,request):
        try:
            notes = Note_User.objects.filter(user_id = request.user.id)
        except Note_User.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def add_note(self,request):
        data = request.data
        data['user'] = request.user.id
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])   
    def get_detail_note(self,request,pk):
        try :
            note = Note_User.objects.get(pk=pk)
        except Note_User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['put'])
    def put_note(self,request,pk):
        note = Note_User.objects.get(pk=pk)
        serializer = NoteSerializer(note, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    @action(detail=False, methods=['delete'])   
    def delete_note(self,request,pk):
        note = Note_User.objects.get(pk=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    

        



    




