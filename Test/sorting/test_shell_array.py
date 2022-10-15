"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import pytest
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa


@pytest.fixture
def orderedlist():
    fname = cf.file_dir + '/Test/Data/' + 'list-small-ordered.csv'
    lst = lt.newList(datastructure='ARRAY_LIST',
                     key='book_id',
                     filename=fname,
                     delimiter=",")
    return lst


@pytest.fixture
def invertedlist():
    fname = cf.file_dir + '/Test/Data/' + 'list-small-inverted.csv'
    lst = lt.newList(datastructure='ARRAY_LIST',
                     key='book_id',
                     filename=fname,
                     delimiter=",")
    return lst


@pytest.fixture
def randomlist():
    fname = cf.file_dir + '/Test/Data/' + 'list-small-random.csv'
    lst = lt.newList(datastructure='ARRAY_LIST',
                     key='book_id',
                     filename=fname,
                     delimiter=",")
    return lst


@pytest.fixture
def emptylist():
    lst = lt.newList(datastructure='ARRAY_LIST',
                     key='book_id')
    return lst


def test_empty_sort(emptylist):
    olist = sa.sort(emptylist, cmpfunction)
    for elem in lt.iterator(olist):
        print(elem)


def test_selection_ordered(orderedlist):
    olist = sa.sort(orderedlist, cmpfunction)
    for elem in lt.iterator(olist):
        print(elem)


def test_selection_inverted(invertedlist):
    olist = sa.sort(invertedlist, cmpfunction)
    for elem in lt.iterator(olist):
        print(elem)


def test_selection_random(randomlist):
    olist = sa.sort(randomlist, cmpfunction)
    for elem in lt.iterator(olist):
        print(elem)


def cmpfunction(elem1, elem2):
    if (int(elem1['book_id']) < int(elem2['book_id'])):
        return True
    return False
