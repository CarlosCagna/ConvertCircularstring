# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ConvertCircularstring
                                 A QGIS plugin
 Convert all geometrys CircularString in LineString
                             -------------------
        begin                : 2017-06-01
        copyright            : (C) 2017 by Carlos Eduardo Cagna
        email                : carlos.cagna@ibge.gov.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ConvertCircularstring class from file ConvertCircularstring.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .convert_circularstring import ConvertCircularstring
    return ConvertCircularstring(iface)
