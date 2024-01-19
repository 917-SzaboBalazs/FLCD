/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_LANG_TAB_H_INCLUDED
# define YY_YY_LANG_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    ARR = 258,
    INT = 259,
    BOOL = 260,
    CHAR = 261,
    STRING = 262,
    IF = 263,
    ELSE = 264,
    WHILE = 265,
    PRINT = 266,
    READINT = 267,
    READSTRING = 268,
    SET = 269,
    GET = 270,
    BOOLCONST = 271,
    CHARCONST = 272,
    STRINGCONST = 273,
    IDENTIFIER = 274,
    INTCONST = 275,
    PLUS = 276,
    MINUS = 277,
    TIMES = 278,
    DIV = 279,
    MOD = 280,
    EQ = 281,
    BIGGER = 282,
    BIGGEREQ = 283,
    LESS = 284,
    LESSEQ = 285,
    EQQ = 286,
    NEG = 287,
    AND = 288,
    OR = 289,
    SEMICOLON = 290,
    OPEN = 291,
    CLOSE = 292,
    SOPEN = 293,
    SCLOSE = 294,
    BRACKETOPEN = 295,
    BRACKETCLOSE = 296,
    COMMA = 297,
    QUOTE = 298,
    SIMPLEQUOTE = 299
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_LANG_TAB_H_INCLUDED  */
