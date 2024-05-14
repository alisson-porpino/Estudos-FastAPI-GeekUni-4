from typing import List, Optional, Any

from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.usuario_model import UsuarioModel
from schemas.usuarios_schema import UsuarioSchemaBase, UsuarioSchemaCreate, UsuarioSchemaUp, UsuariosSchemaArtigos
from core.deps import get_session, get_current_user
from core.security import gerar_hash_senha
from core.auth import autenticar, criar_token_acesso


router = APIRouter()

# GET Logado
@router.get('/logado', response_model=UsuarioSchemaBase)
