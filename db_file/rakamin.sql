PGDMP                         {         	   rakamindb    13.5    13.5 $    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    66471 	   rakamindb    DATABASE     i   CREATE DATABASE rakamindb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_Indonesia.1252';
    DROP DATABASE rakamindb;
                rakamin    false            �            1259    66550    tconversation    TABLE     �   CREATE TABLE public.tconversation (
    conversation_id integer NOT NULL,
    room_id integer,
    member_id integer,
    message character varying,
    created_at timestamp without time zone
);
 !   DROP TABLE public.tconversation;
       public         heap    rakamin    false            �            1259    66548 !   tconversation_conversation_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tconversation_conversation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.tconversation_conversation_id_seq;
       public          rakamin    false    207            �           0    0 !   tconversation_conversation_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.tconversation_conversation_id_seq OWNED BY public.tconversation.conversation_id;
          public          rakamin    false    206            �            1259    66494    tmember    TABLE     �   CREATE TABLE public.tmember (
    member_id integer NOT NULL,
    username character varying(50),
    email character varying(50),
    password character varying(200),
    member_type character varying,
    created_at timestamp without time zone
);
    DROP TABLE public.tmember;
       public         heap    rakamin    false            �            1259    66492    tmember_member_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tmember_member_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.tmember_member_id_seq;
       public          rakamin    false    201            �           0    0    tmember_member_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.tmember_member_id_seq OWNED BY public.tmember.member_id;
          public          rakamin    false    200            �            1259    66505    troom    TABLE     �   CREATE TABLE public.troom (
    room_id integer NOT NULL,
    room_name character varying(20),
    created_at timestamp without time zone
);
    DROP TABLE public.troom;
       public         heap    rakamin    false            �            1259    66503    troom_room_id_seq    SEQUENCE     �   CREATE SEQUENCE public.troom_room_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.troom_room_id_seq;
       public          rakamin    false    203            �           0    0    troom_room_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.troom_room_id_seq OWNED BY public.troom.room_id;
          public          rakamin    false    202            �            1259    66514    troommember    TABLE     t   CREATE TABLE public.troommember (
    roommember_id integer NOT NULL,
    room_id integer,
    member_id integer
);
    DROP TABLE public.troommember;
       public         heap    rakamin    false            �            1259    66512    troommember_roommember_id_seq    SEQUENCE     �   CREATE SEQUENCE public.troommember_roommember_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.troommember_roommember_id_seq;
       public          rakamin    false    205            �           0    0    troommember_roommember_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.troommember_roommember_id_seq OWNED BY public.troommember.roommember_id;
          public          rakamin    false    204            9           2604    66553    tconversation conversation_id    DEFAULT     �   ALTER TABLE ONLY public.tconversation ALTER COLUMN conversation_id SET DEFAULT nextval('public.tconversation_conversation_id_seq'::regclass);
 L   ALTER TABLE public.tconversation ALTER COLUMN conversation_id DROP DEFAULT;
       public          rakamin    false    207    206    207            6           2604    66497    tmember member_id    DEFAULT     v   ALTER TABLE ONLY public.tmember ALTER COLUMN member_id SET DEFAULT nextval('public.tmember_member_id_seq'::regclass);
 @   ALTER TABLE public.tmember ALTER COLUMN member_id DROP DEFAULT;
       public          rakamin    false    200    201    201            7           2604    66508    troom room_id    DEFAULT     n   ALTER TABLE ONLY public.troom ALTER COLUMN room_id SET DEFAULT nextval('public.troom_room_id_seq'::regclass);
 <   ALTER TABLE public.troom ALTER COLUMN room_id DROP DEFAULT;
       public          rakamin    false    203    202    203            8           2604    66517    troommember roommember_id    DEFAULT     �   ALTER TABLE ONLY public.troommember ALTER COLUMN roommember_id SET DEFAULT nextval('public.troommember_roommember_id_seq'::regclass);
 H   ALTER TABLE public.troommember ALTER COLUMN roommember_id DROP DEFAULT;
       public          rakamin    false    205    204    205            �          0    66550    tconversation 
   TABLE DATA           a   COPY public.tconversation (conversation_id, room_id, member_id, message, created_at) FROM stdin;
    public          rakamin    false    207   �)       �          0    66494    tmember 
   TABLE DATA           `   COPY public.tmember (member_id, username, email, password, member_type, created_at) FROM stdin;
    public          rakamin    false    201   u*       �          0    66505    troom 
   TABLE DATA           ?   COPY public.troom (room_id, room_name, created_at) FROM stdin;
    public          rakamin    false    203   {-       �          0    66514    troommember 
   TABLE DATA           H   COPY public.troommember (roommember_id, room_id, member_id) FROM stdin;
    public          rakamin    false    205   �-       �           0    0 !   tconversation_conversation_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.tconversation_conversation_id_seq', 10, true);
          public          rakamin    false    206            �           0    0    tmember_member_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.tmember_member_id_seq', 16, true);
          public          rakamin    false    200            �           0    0    troom_room_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.troom_room_id_seq', 13, true);
          public          rakamin    false    202            �           0    0    troommember_roommember_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.troommember_roommember_id_seq', 41, true);
          public          rakamin    false    204            A           2606    66558     tconversation tconversation_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.tconversation
    ADD CONSTRAINT tconversation_pkey PRIMARY KEY (conversation_id);
 J   ALTER TABLE ONLY public.tconversation DROP CONSTRAINT tconversation_pkey;
       public            rakamin    false    207            ;           2606    66502    tmember tmember_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.tmember
    ADD CONSTRAINT tmember_pkey PRIMARY KEY (member_id);
 >   ALTER TABLE ONLY public.tmember DROP CONSTRAINT tmember_pkey;
       public            rakamin    false    201            =           2606    66510    troom troom_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.troom
    ADD CONSTRAINT troom_pkey PRIMARY KEY (room_id);
 :   ALTER TABLE ONLY public.troom DROP CONSTRAINT troom_pkey;
       public            rakamin    false    203            ?           2606    66519    troommember troommember_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.troommember
    ADD CONSTRAINT troommember_pkey PRIMARY KEY (roommember_id);
 F   ALTER TABLE ONLY public.troommember DROP CONSTRAINT troommember_pkey;
       public            rakamin    false    205            E           2606    66564 *   tconversation tconversation_member_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tconversation
    ADD CONSTRAINT tconversation_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.tmember(member_id);
 T   ALTER TABLE ONLY public.tconversation DROP CONSTRAINT tconversation_member_id_fkey;
       public          rakamin    false    2875    201    207            D           2606    66559 (   tconversation tconversation_room_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tconversation
    ADD CONSTRAINT tconversation_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.troom(room_id);
 R   ALTER TABLE ONLY public.tconversation DROP CONSTRAINT tconversation_room_id_fkey;
       public          rakamin    false    2877    203    207            C           2606    66525 &   troommember troommember_member_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.troommember
    ADD CONSTRAINT troommember_member_id_fkey FOREIGN KEY (member_id) REFERENCES public.tmember(member_id);
 P   ALTER TABLE ONLY public.troommember DROP CONSTRAINT troommember_member_id_fkey;
       public          rakamin    false    205    201    2875            B           2606    66520 $   troommember troommember_room_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.troommember
    ADD CONSTRAINT troommember_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.troom(room_id);
 N   ALTER TABLE ONLY public.troommember DROP CONSTRAINT troommember_room_id_fkey;
       public          rakamin    false    2877    203    205            �   y   x�e�1�0Eg�> �l7I�,\��R�X)CoO��7��_� ��l����i����j�?�Y]�WP�y�0��H�u�9c>v�n'�=�+p��d�=���}��yv�Ӣ3�"~�&�      �   �  x���AO#9��ɯ���DU.���iga�4D�a+��R��$�L���iw��U�ԯ��[���{Ɓ����M����j\�n~:p���L�&���$D��i��[?��O/�7����B�I��-(��z}�uv�U������amE��c�����污ϊ���XZ��R�$���]=�l�/��L�O@�>��8�����U����O����������٨TEPWb����&K��j�h�j�5k�FT%�D��d%���!���~�}��Ggӳ|����i��t��8`I��0�'s5�`ѡb�͌=����/�ɵ���.D�?�bs�^�3�z��_�^pnۣ���|=�9�#��r��

�5gȚ]�}�*�q
\-f�cvB>���������>ؓ���۳�"y�};�� d�����W�?a@��stl�sc�"%�E���JA���ޮ��>��������zj����ß�]i,7�j	=�=}�РV5��V�`��$-,0J�^"�����H�1��{��w7o������_f��t�YW��Q�ʬ�H�%,!Ʀ�.uf�j�(��zc�u�Y/N��ۯ>:����� b���y���U��@�3��r�0���!���@j�S �b���tެ����T���3+ʆ�q|-�� '&.�%t2�0�wϻk^8���vs\N����y��>;�Ir�� �RQ}��Ћ��*S��Xr�<��$���y�pG�i��x8� ��      �   m   x��̱@0 ���+����W�(X�6�`	��X���j�t��؜\�!c��Q�G��
��p�nݾ��4�eJhd2������!�7)������G��'��'x      �   C   x����0��x��$iv��sxI��q�n$�#ю](
tH͚���Ӭ~���@�D��Brd�{ ����     