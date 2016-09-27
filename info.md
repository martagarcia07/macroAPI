### POSTGRESS TABLES USERS AND MACROS

postgres=# \d users_db
                                        Tabla «public.users_db»
   Columna   |          Tipo          |                          Modificadores                          
-------------+------------------------+-----------------------------------------------------------------
 id          | integer                | not null valor por omisión nextval('users_db_id_seq'::regclass)
 username    | character varying(20)  | not null
 pass        | character(40)          | not null
 name        | character varying(20)  | not null
 surname     | character varying(20)  | not null
 last_online | date                   | not null
 birthdate   | date                   | not null
 height_cm   | integer                | not null
 weight_kg   | numeric                | not null
 email       | character varying(100) | not null
Índices:
    "utilisateur_pkey" PRIMARY KEY, btree (id)


postgres=# \d macros_db
      Tabla «public.macros_db»
 Columna  |  Tipo   | Modificadores 
----------+---------+---------------
 id       | integer | not null
 product  | text    | not null
 producto | text    | not null
 cal      | integer | not null
 fat      | integer | not null
 pro      | integer | not null
 car      | integer | not null
 porttype | text    | not null
 port     | integer | not null
 type     | text    | not null
Índices:
    "macros_db_pkey" PRIMARY KEY, btree (id)


postgres=# \d macros_rate_db
   Tabla «public.macros_rate_db»
 Columna |  Tipo   | Modificadores 
---------+---------+---------------
 id      | integer | not null
 product | integer | 
 rate    | integer | not null
Índices:
    "macros_rate_db_pkey" PRIMARY KEY, btree (id)
Restricciones de llave foránea:
    "macros_rate_db_product_fkey" FOREIGN KEY (product) REFERENCES macros_db(id)









#######################################################################################
CREATE TABLE users_db
(
  id serial NOT NULL,
  username character varying(20) NOT NULL,
  pass character(40) NOT NULL,
  name character varying(20) NOT NULL,
  surname character varying(20) NOT NULL,
  last_online date NOT NULL,
  birthdate date NOT NULL,
  height_cm integer NOT NULL,
  weight_kg decimal NOT NULL,
  email character varying(100) NOT NULL,
  CONSTRAINT utilisateur_pkey PRIMARY KEY (id)
);



CREATE TABLE macros_rate_db(
   id INT PRIMARY KEY     NOT NULL,
   product  int references macros_db(id),
   rate int NOT NULL
);

CREATE TABLE macros_db(
   id INT PRIMARY KEY     NOT NULL,
   product TEXT NOT NULL,
   producto TEXT NOT NULL,
   cal INT NOT NULL,
   fat INT NOT NULL,
   pro INT NOT NULL,
   car INT NOT NULL,
   portType TEXT NOT NULL,
   port INT NOT NULL,
   type TEXT NOT NULL
);


### MONGODB TABLES USERMACROS

