# Personal-IO
-Aplicacion para el control de entrada y salida de personal

> Requerimientos:
* Python 2 o Python 3
* Sqlite3
* PyQt4

### Version
1.0.0



# Build .deb

## 1. Dependencies generic to build a package

* git.
* git-buildpackage.
* build-essential.

* >  git-buildpackage and build-essentia are Meta-Packages that have all depends generic to build a packages

Execute:

```bash
apt install git-buildpackage build-essential
``` 

## 2. To create a clean .deb, we will create an environment in pbuilder

#### Install pbuilder:

```bash
$ apt install pbuilder
```

#### Now create the pbuilder to build the package

Execute AMD64:

```bash
$ DIST=jessie ARCH=amd64 git-pbuilder create
```

and i386:

```bash
$ DIST=jessie ARCH=i386 git-pbuilder create
```

## And now yes, you can Build the package


#### 3. Build without pbuilder:


Root the project:

```bash
$ cd gescolar-estadistico-deb/ 
``` 

Execute in the root of the project:

```bash
$ gbp buildpackage -tc --git-tag --git-retag -uc -us --git-debian-branch="branch"
```

#### Build with pbuilder and a package amd64

```bash
$ gbp buildpackage --git-pbuilder --git-dist=jessie --git-arch=amd64 --git-upstream-tree="branch" -us -uc 
``` 

#### i386 package:

```bash
$ gbp buildpackage --git-pbuilder --git-dist=jessie --git-arch=i386 --git-upstream-tree="branch" -us -uc 
```

#### build without control version

Execute in the root of the project:

```bash
$ debuild -us -uc
```

# SOURCEs

[https://github.com/vpino/canaima-judge] [https://github.com/joseguerrero/curso-empaquetamiento] [http://huntingbears.com.ve/creando-un-metapaquete-a-la-canaima-con-canaima-desarrollador.html]







License
----
MIT

**Israel Lugo (Hostelix)**
