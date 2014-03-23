wrap-u
================

Sublime plugin for wrap a selection with u() and remove units

Build to use in [bebop](https://github.com/arthurgouveia/bebop) project

In bebop, most of time you don`t use units in px, you use u(value), example: 

  .foo {
    padding-top: u(10);
  }

So this plugin helps you do write normal code (a.k.a in px) and easily convert to u() notation

if you write `padding-top: 10px;`, select `10px` and type Ctrl + u, it transform to u(10)

Enjoy.
