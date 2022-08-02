# ibis-tutorials

This series of notebooks and modules will introduce you to Ibis and familiarize you with its core concepts.
We will focus on the [DuckDB](https://duckdb.org/) backend since it is the easiest to set up and has the most support,
and we will use mock farm data to help show various practical use cases for Ibis in data and analytics projects.

The only nice to have is a basic understanding of Python, as environment setup can be done through Project Binder.
Everything else will be explained throughout, and a direct link to Binder is at the bottom of this ReadMe.

While the following tutorials will use the DuckDB backend, one key feature of Ibis is engine agnosticism.
You may use any backend to complete the exercises after you have established a connection and loaded
the provided data.

The first tutorial notebook, Chapter 1 - Establishing a Connection, will walk you through how to connect to a backend.
All tutorials after that will use the `backend_access.py` module to connect to a backend using the function `connect`,
which will default to connecting using the DuckDB backend.
This function's comments will detail how to set up your connection and what you need to know before using it
so you can use it going forward with your backend of choice.

The Ibis project is still in development, and new backends are being added regularly.
Your backend of choice might not (yet!) support a function that the tutorial calls for.
If this occurs, please open up a ticket in the relevant repository requesting that feature's inclusion.

You can find the Ibis project homepage at [ibis-project.org](https://ibis-project.org/docs/),
and the home repository for the project at [GitHub](https://github.com/ibis-project).

## How to Use These Notebooks

This repository has a lot of information in it, so it's a good idea to understand the structure to better
optimize how you extract this information.

The `tutorials/` directory contains notebooks that will walk you through how to get started with Ibis.
It's recommended that you at least skim some of them first before moving on.

The `schematics/` directory contains a set of how-to guides, demonstrating different ways of applying Ibis
to your projects.

### `tutorials/`

While the `tutorials/` notebooks are geared towards new users, it is recommended you at least skim the notebooks,
as they contain some useful information.

Each notebook is one chapter containing a self-contained (after data and connection setup) set of exercises that
will help you learn a core Ibis concept.

Exercises a prompts that require you, in most cases, to use the information in the prompt and previous exercises to perform
some action.
Sometimes a prompt will tell you what the solution is.
**In that case: do not copy and paste the solution.**
Type it out.
Copy+paste will not reinforce your learning.

Solutions are provided immediately after each prompt in case you get stuck or want to check your work.
Again, **do not copy and paste the solution**.
Type it out.

Exercises within a chapter will often rely on other exercises within that chapter, so avoid skiping exercises.

## Installation

`environment.yml` should be enough to get you started through Docker,
but, if you wish to build the environment yourself,
you need `ibis-framework` installed for the backend you care about.

For pip installation, the format typically follows `pip install ibis-framework[{{ backend }}]`,
and for conda or mamba installation: `{{ conda/mamba }} install -c conda-forge ibis-framework[{{ backend }}]`.

For example, installing the DuckDB backend:

```
pip install ibis-framework[duckdb]
```

or, conda:

```
conda install -c conda-forge ibis-framework[duckdb]
```

If you wish to use a different backend, you can find supported backends using `ibis-framework[<backend>]`.
