# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cursos.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'cursos.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ursos.proto\x12\x06\x63ursos\x1a\x1bgoogle/protobuf/empty.proto\"l\n\x05\x43urso\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bnombreCurso\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scripcion\x18\x03 \x01(\t\x12\x16\n\x0enombreProfesor\x18\x04 \x01(\t\x12\x15\n\rnumeroDeHoras\x18\x05 \x01(\x05\"o\n\x14InsertarCursoRequest\x12\x13\n\x0bnombreCurso\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scripcion\x18\x02 \x01(\t\x12\x16\n\x0enombreProfesor\x18\x03 \x01(\t\x12\x15\n\rnumeroDeHoras\x18\x04 \x01(\x05\"U\n\x15InsertarCursoResponse\x12\r\n\x05\x65xito\x18\x01 \x01(\x08\x12\x0f\n\x07mensaje\x18\x02 \x01(\t\x12\x1c\n\x05\x63urso\x18\x03 \x01(\x0b\x32\r.cursos.Curso\"6\n\x15ObtenerCursosResponse\x12\x1d\n\x06\x63ursos\x18\x01 \x03(\x0b\x32\r.cursos.Curso\"!\n\x13ObtenerCursoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"T\n\x14ObtenerCursoResponse\x12\r\n\x05\x65xito\x18\x01 \x01(\x08\x12\x0f\n\x07mensaje\x18\x02 \x01(\t\x12\x1c\n\x05\x63urso\x18\x03 \x01(\x0b\x32\r.cursos.Curso\"}\n\x16\x41\x63tualizarCursoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bnombreCurso\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scripcion\x18\x03 \x01(\t\x12\x16\n\x0enombreProfesor\x18\x04 \x01(\t\x12\x15\n\rnumeroDeHoras\x18\x05 \x01(\x05\"W\n\x17\x41\x63tualizarCursoResponse\x12\r\n\x05\x65xito\x18\x01 \x01(\x08\x12\x0f\n\x07mensaje\x18\x02 \x01(\t\x12\x1c\n\x05\x63urso\x18\x03 \x01(\x0b\x32\r.cursos.Curso\"\"\n\x14\x45liminarCursoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"7\n\x15\x45liminarCursoResponse\x12\r\n\x05\x65xito\x18\x01 \x01(\x08\x12\x0f\n\x07mensaje\x18\x02 \x01(\t2\x91\x03\n\x0c\x43ursoService\x12L\n\rInsertarCurso\x12\x1c.cursos.InsertarCursoRequest\x1a\x1d.cursos.InsertarCursoResponse\x12\x46\n\rObtenerCursos\x12\x16.google.protobuf.Empty\x1a\x1d.cursos.ObtenerCursosResponse\x12I\n\x0cObtenerCurso\x12\x1b.cursos.ObtenerCursoRequest\x1a\x1c.cursos.ObtenerCursoResponse\x12R\n\x0f\x41\x63tualizarCurso\x12\x1e.cursos.ActualizarCursoRequest\x1a\x1f.cursos.ActualizarCursoResponse\x12L\n\rEliminarCurso\x12\x1c.cursos.EliminarCursoRequest\x1a\x1d.cursos.EliminarCursoResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cursos_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CURSO']._serialized_start=53
  _globals['_CURSO']._serialized_end=161
  _globals['_INSERTARCURSOREQUEST']._serialized_start=163
  _globals['_INSERTARCURSOREQUEST']._serialized_end=274
  _globals['_INSERTARCURSORESPONSE']._serialized_start=276
  _globals['_INSERTARCURSORESPONSE']._serialized_end=361
  _globals['_OBTENERCURSOSRESPONSE']._serialized_start=363
  _globals['_OBTENERCURSOSRESPONSE']._serialized_end=417
  _globals['_OBTENERCURSOREQUEST']._serialized_start=419
  _globals['_OBTENERCURSOREQUEST']._serialized_end=452
  _globals['_OBTENERCURSORESPONSE']._serialized_start=454
  _globals['_OBTENERCURSORESPONSE']._serialized_end=538
  _globals['_ACTUALIZARCURSOREQUEST']._serialized_start=540
  _globals['_ACTUALIZARCURSOREQUEST']._serialized_end=665
  _globals['_ACTUALIZARCURSORESPONSE']._serialized_start=667
  _globals['_ACTUALIZARCURSORESPONSE']._serialized_end=754
  _globals['_ELIMINARCURSOREQUEST']._serialized_start=756
  _globals['_ELIMINARCURSOREQUEST']._serialized_end=790
  _globals['_ELIMINARCURSORESPONSE']._serialized_start=792
  _globals['_ELIMINARCURSORESPONSE']._serialized_end=847
  _globals['_CURSOSERVICE']._serialized_start=850
  _globals['_CURSOSERVICE']._serialized_end=1251
# @@protoc_insertion_point(module_scope)