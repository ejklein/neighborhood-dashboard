# import xml
#
#
# from common import *
# from osm_common import *
#
# def retrieveClosestRoad(roads, lat, lon):
#     shortestDistance = -1
#     closestRoad = -1
#     vectA = numpy.array([lat, lon])
#     shortestSegment = []
#     for rid in roads:
#         points = roads[rid]["points"]
#         point1 = points[0]
#         for point in points[1::]:
#             point2 = point
#             if point1 == point2:
#                 print 'Points on road are identical'
#                 continue
#             vect1 = numpy.array(point1)
#             vect2 = numpy.array(point2)
#             distance = determineDistance(vect1, vect2, vectA)
#             if shortestDistance == -1 or shortestDistance > distance:
#                 shortestDistance = distance
#                 closestRoad = rid
#                 shortestSegment = [point1, point2]
#             point1 = point2
#     if closestRoad == -1:
#         return {}
#     result = roads[closestRoad]
#     segment = { 'distance': shortestDistance, 'points': shortestSegment }
#     if shortestDistance == 0.0:
#         segment['segment-point'] = [lat, lon]
#     else:
#         segment['segment-point'] = determinePointOnSegment(lat, lon, shortestSegment)
#     result['segment'] = segment
#     return result
#
# lat = 52.77076
# lon = -2.544535
#
# outputfolder = 'output'
# osm_output_folder = os.path.join(outputfolder, OSMDATAFOLDER)
#
# downloadOsm('7708.osm', lat, lon, osm_output_folder)
# data = readOsm('7708.osm', osm_output_folder)
# roads = parseOsm(data)
#
# result = {}
# result['roads'] = retrieveClosestRoad(roads, lat, lon)
#
# print result

# road_data = {"roads":
#                  {"points": [[52.7402029, -1.8755707], [52.7401487, -1.8756335], [52.7400635, -1.8757324], [52.739847, -1.8758394], [52.7397397, -1.8759564], [52.7396491, -1.8760525], [52.7395813, -1.8762029], [52.7394521, -1.8764498], [52.7393456, -1.8765811], [52.7391823, -1.8767341], [52.7391568, -1.876752], [52.7389906, -1.8769594]],
#                   "segment": {"distance": 4.2195456666296162e-08, "points": [[52.7395813, -1.8762029], [52.7394521, -1.8764498]],
#                               "segment-point": [52.739527997684355, -1.8763047602301295]},
#                   "tags": {"source": "Bing, OS_Locator", "name": "Wordsworth Close", "highway": "residential"}},
#              "pois": {"amenity": {"place_of_worship": [{"count": 1, "distance": 562.3483373205014, "points": [[52.7416633, -1.8683293], [52.7416791, -1.8686422], [52.7416015, -1.8686529], [52.7415857, -1.86834], [52.7416633, -1.8683293]], "average_distance": 576.039636148863, "tags": {"religion": "christian", "amenity": "place_of_worship", "name": "Handsacre Methodist Church", "denomination": "methodist"}}], "school": [{"distance": 788.2984808176146, "points": [[52.7384565, -1.8648752], [52.7388343, -1.8646814], [52.7388616, -1.8624635], [52.7388681, -1.8622699], [52.7386226, -1.8621229], [52.7381235, -1.8613412], [52.7378682, -1.8639606], [52.7384565, -1.8648752]], "tags": {"amenity": "school"}}, {"count": 2, "distance": 748.2482614300812, "points": [[52.7432761, -1.8866251], [52.743402, -1.8861864], [52.7435586, -1.886309], [52.743609, -1.886133], [52.7434833, -1.8860346], [52.7435744, -1.8857168], [52.743461, -1.885628], [52.7431935, -1.8865604], [52.7432761, -1.8866251]], "average_distance": 831.7944365701372, "tags": {"building": "school", "amenity": "school", "name": "Croft Primary School", "addr:street": "Rugeley Road"}}], "post_box": [{"count": 2, "distance": 244.00876409375252, "points": [[52.7418357, -1.8755]], "average_distance": 483.41690800426056, "tags": {"amenity": "post_box", "ref": "WS15 312"}}, {"distance": 722.8250519147686, "points": [[52.7425595, -1.8667493]], "tags": {"amenity": "post_box", "ref": "WS15", "fixme": "Resurvey to complete box number if ref key"}}], "veterinary": [{"count": 1, "distance": 307.257307212886, "points": [[52.7419633, -1.8790418]], "average_distance": 307.257307212886, "tags": {"amenity": "veterinary", "name": "Pool House Veterinary Clinic"}}], "pub": [{"distance": 632.301308056317, "points": [[52.7418822, -1.8677198], [52.7419699, -1.8677212], [52.7419697, -1.867762], [52.742024, -1.8677629], [52.7420243, -1.8677223], [52.7420948, -1.8677234], [52.7420959, -1.8675225], [52.7420598, -1.8675219], [52.7420594, -1.8675895], [52.7420023, -1.8675886], [52.7420021, -1.8676217], [52.7419403, -1.8676207], [52.7419404, -1.8675941], [52.7418829, -1.8675932], [52.7418822, -1.8677198]], "tags": {"building": "pub", "website": "http://www.theoldepeculiar.co.uk/", "amenity": "pub", "name": "The Olde Peculiar", "source": "survey", "brewery": "Theakston"}}, {"count": 2, "distance": 453.3890140640647, "points": [[52.7418357, -1.8821472]], "average_distance": 629.3970417063672, "tags": {"amenity": "pub", "name": "The Swan Inn"}}], "parking": [{"distance": 218.94763035189538, "points": [[52.7416157, -1.8772183], [52.7416287, -1.8771513], [52.7415978, -1.8771325], [52.7415832, -1.8770547], [52.7413932, -1.8770279], [52.74139, -1.8770949], [52.7413461, -1.8770949], [52.7413332, -1.8772076], [52.7413445, -1.8772961], [52.7413494, -1.8774007], [52.74139, -1.8773927], [52.7414046, -1.8774409], [52.7416092, -1.8773229], [52.7416157, -1.8772183]], "tags": {"amenity": "parking"}}, {"distance": 625.1024550185965, "points": [[52.7367597, -1.8684964], [52.7369748, -1.8684977], [52.7369514, -1.8687064], [52.7367532, -1.8687136], [52.7367597, -1.8684964]], "tags": {"amenity": "parking"}}, {"count": 4, "distance": 183.27311932030563, "points": [[52.7393683, -1.8737368], [52.7394495, -1.8731843], [52.739339, -1.873136], [52.7392871, -1.8734364], [52.7392578, -1.8734418], [52.7392416, -1.8735169], [52.7389006, -1.873372], [52.7388811, -1.8734739], [52.7393683, -1.8737368]], "average_distance": 373.43496447981386, "tags": {"amenity": "parking"}}, {"distance": 678.2872389654116, "points": [[52.7420355, -1.8670853], [52.742013, -1.8674545], [52.742109, -1.8674648], [52.7421475, -1.8674258], [52.7422258, -1.8674394], [52.7422646, -1.8673445], [52.7422119, -1.8672032], [52.7421536, -1.8671479], [52.7420355, -1.8670853]], "tags": {"access": "customers", "amenity": "parking"}}], "post_office": [{"count": 1, "distance": 249.9964286650557, "points": [[52.7419064, -1.8756069]], "average_distance": 249.9964286650557, "tags": {"source": "survey", "amenity": "post_office"}}]}, "landuse": {"grass": [{"distance": 467.7541644444348, "points": [[52.7416924, -1.8702717], [52.7419244, -1.8702913], [52.7421181, -1.8703588], [52.7422314, -1.8703718], [52.7422921, -1.8701541], [52.7422394, -1.8697275], [52.7420773, -1.8688719], [52.7420443, -1.8685758], [52.7420364, -1.868282], [52.7421194, -1.8679641], [52.7419824, -1.8682742], [52.7417741, -1.8687456], [52.7416581, -1.8690722], [52.7416173, -1.8693552], [52.7416199, -1.8698341], [52.7416397, -1.8702195], [52.7416924, -1.8702717]], "tags": {"source": "Bing", "landuse": "grass", "leisure": "park"}}, {"count": 5, "distance": 27.69962052030919, "points": [[52.7406615, -1.8766266], [52.7405176, -1.876956], [52.7404051, -1.8768619], [52.7403669, -1.8768495], [52.7402552, -1.877003], [52.7403864, -1.877356], [52.7405578, -1.8777592], [52.7404865, -1.8778343], [52.7401716, -1.8781197], [52.7401482, -1.8780794], [52.7400465, -1.8782108], [52.7398821, -1.8780572], [52.7394969, -1.8783117], [52.7391057, -1.877465], [52.7395852, -1.8768481], [52.739948, -1.8762785], [52.7400598, -1.8762327], [52.7400755, -1.8763342], [52.7404399, -1.8761645], [52.7406615, -1.8766266]], "average_distance": 440.2782360378488, "tags": {"landuse": "grass"}}, {"distance": 610.1018117771575, "points": [[52.7432471, -1.8694717], [52.7432155, -1.8695533], [52.742736, -1.8695962], [52.7427224, -1.8692154], [52.7427873, -1.869151], [52.7428523, -1.8689954], [52.7428942, -1.8689902], [52.7430244, -1.868974], [52.7431348, -1.8689418], [52.74319, -1.8692532], [52.7432471, -1.8694717]], "tags": {"source": "Bing", "landuse": "grass", "leisure": "park"}}, {"distance": 610.1018117771575, "points": [[52.7432471, -1.8694717], [52.7433524, -1.8693709], [52.7432777, -1.8708142], [52.7433849, -1.8718227], [52.7434596, -1.8722143], [52.7433362, -1.8718547], [52.743177, -1.8714955], [52.7431413, -1.8714255], [52.7431409, -1.8713183], [52.7431495, -1.8708918], [52.7430886, -1.8706396], [52.7427771, -1.8706396], [52.742736, -1.8695962], [52.74285, -1.8689847], [52.7431336, -1.868936], [52.7432375, -1.8694042], [52.7432428, -1.8694417], [52.7432471, -1.8694717]], "tags": {"source": "Bing", "landuse": "grass", "leisure": "park"}}, {"distance": 622.0499989200596, "points": [[52.741719, -1.8677762], [52.7417275, -1.8675568], [52.7415585, -1.8675466], [52.7415399, -1.8676166], [52.7415404, -1.8676931], [52.7415681, -1.8677342], [52.7416501, -1.8677575], [52.741719, -1.8677762]], "tags": {"source": "Bing", "landuse": "grass"}}], "reservoir": [{"count": 3, "distance": 696.2703283781167, "points": [[52.7445355, -1.8689845], [52.7445227, -1.8694229], [52.7444809, -1.8694853], [52.7443613, -1.8694754], [52.7444609, -1.8689766], [52.7445355, -1.8689845]], "average_distance": 750.6871155510211, "tags": {"source": "Bing", "landuse": "reservoir"}}, {"distance": 790.2001392116983, "points": [[52.7452552, -1.8690588], [52.7452476, -1.8695135], [52.7452227, -1.8695529], [52.7450646, -1.8695468], [52.7450248, -1.8695068], [52.7450315, -1.8690319], [52.7450438, -1.8689987], [52.7452245, -1.8690057], [52.7452552, -1.8690588]], "tags": {"source": "Bing", "landuse": "reservoir"}}, {"distance": 750.6409636925699, "points": [[52.7449916, -1.8694553], [52.7449636, -1.8695149], [52.7448008, -1.8694977], [52.7447784, -1.869458], [52.7447888, -1.8690593], [52.7448104, -1.8690117], [52.744966, -1.8690196], [52.7449916, -1.8690713], [52.7449916, -1.8694553]], "tags": {"source": "Bing", "landuse": "reservoir"}}], "orchard": [{"count": 1, "distance": 516.4200986407017, "points": [[52.742736, -1.8695962], [52.7427771, -1.8706396], [52.7430886, -1.8706396], [52.7431071, -1.8704424], [52.7431776, -1.8702959], [52.7432367, -1.8700781], [52.7432155, -1.8695533], [52.742736, -1.8695962]], "average_distance": 561.224063429874, "tags": {"landuse": "orchard"}}], "residential": [{"distance": 271.89773417467717, "points": [[52.7410366, -1.8730072], [52.7407448, -1.8738857], [52.7407005, -1.8746756], [52.7406746, -1.8751371], [52.7405655, -1.8754654], [52.7409285, -1.8756885], [52.7409374, -1.8761565], [52.7407647, -1.876482], [52.7406615, -1.8766266], [52.7405176, -1.876956], [52.7404051, -1.8768619], [52.7403669, -1.8768495], [52.7402552, -1.877003], [52.7403864, -1.877356], [52.7405578, -1.8777592], [52.7404865, -1.8778343], [52.7401716, -1.8781197], [52.7401482, -1.8780794], [52.7400465, -1.8782108], [52.7398821, -1.8780572], [52.7394969, -1.8783117], [52.7400972, -1.8795778], [52.7396146, -1.8801054], [52.740138, -1.8814356], [52.7399873, -1.8819119], [52.7398097, -1.8819722], [52.7391644, -1.8818721], [52.7384568, -1.8815825], [52.7384496, -1.8820449], [52.7383643, -1.8826899], [52.7381913, -1.8826502], [52.7381156, -1.8831403], [52.7383523, -1.8832475], [52.7386803, -1.8835352], [52.738239, -1.8841941], [52.7388734, -1.8852498], [52.7394501, -1.8844124], [52.7396856, -1.8843528], [52.739837, -1.8842615], [52.740344, -1.884972], [52.7404425, -1.8852696], [52.7399283, -1.8864365], [52.7408558, -1.8878733], [52.7423071, -1.8861904], [52.7429266, -1.8867559], [52.743042, -1.8861169], [52.743078, -1.8855613], [52.7431131, -1.8853427], [52.7428126, -1.8837091], [52.7428062, -1.8836744], [52.7424133, -1.8839171], [52.7422591, -1.8828375], [52.74211, -1.8828106], [52.7422711, -1.8817356], [52.7423736, -1.8810767], [52.7426581, -1.8799327], [52.7424221, -1.8797131], [52.7427256, -1.8788207], [52.7421943, -1.8782621], [52.7425956, -1.8764245], [52.7426484, -1.8759998], [52.7424634, -1.8745591], [52.7424762, -1.8738976], [52.7419714, -1.8727149], [52.7417464, -1.8721519], [52.7415454, -1.8722085], [52.7411976, -1.8723628], [52.7410366, -1.8730072]], "tags": {"source": "Bing", "landuse": "residential"}}, {"distance": 408.18094514864964, "points": [[52.7412258, -1.8708778], [52.7401483, -1.8685262], [52.7393044, -1.8670387], [52.7389254, -1.8663116], [52.7377052, -1.8643546], [52.7359068, -1.8618211], [52.7349522, -1.8605733], [52.7347124, -1.8616479], [52.7345048, -1.8624078], [52.7341314, -1.862116], [52.7340156, -1.8626347], [52.7344388, -1.8629486], [52.7350819, -1.8636912], [52.7358142, -1.8644775], [52.7357315, -1.8648133], [52.7355133, -1.8656132], [52.7352852, -1.8673277], [52.7350538, -1.8687091], [52.7352984, -1.868802], [52.7370044, -1.8688074], [52.7369416, -1.8699814], [52.7372259, -1.8707458], [52.7374044, -1.8707895], [52.7381672, -1.8709975], [52.7381489, -1.8705548], [52.7383026, -1.8703734], [52.7387528, -1.8707724], [52.7391701, -1.8709296], [52.7400338, -1.8712137], [52.7405938, -1.871383], [52.740872, -1.8712077], [52.7412258, -1.8708778]], "tags": {"source": "Bing", "landuse": "residential"}}, {"distance": 955.8641928131659, "points": [[52.7388681, -1.8622699], [52.7390048, -1.8612414], [52.7391913, -1.8605349], [52.7396062, -1.8597222], [52.7400821, -1.8599135], [52.7406545, -1.860264], [52.7411176, -1.8606358], [52.7418251, -1.8612998], [52.7424167, -1.8618416], [52.74251, -1.8622293], [52.7426933, -1.8625321], [52.7427415, -1.8629517], [52.7427865, -1.8633394], [52.7429763, -1.8640353], [52.7433332, -1.8646408], [52.7431284, -1.8650083], [52.7431494, -1.8656369], [52.7432132, -1.8659038], [52.7435285, -1.8657701], [52.7436194, -1.8660202], [52.7437705, -1.8662646], [52.7440581, -1.8666779], [52.7441422, -1.867046], [52.7441172, -1.8676131], [52.7440035, -1.8681201], [52.7435609, -1.8686073], [52.7434737, -1.8687174], [52.7434096, -1.8691899], [52.7433374, -1.8692156], [52.7432375, -1.8694042], [52.7431336, -1.868936], [52.74285, -1.8689847], [52.742736, -1.8695962], [52.7427771, -1.8706396], [52.7430886, -1.8706396], [52.7431495, -1.8708918], [52.7431387, -1.8709789], [52.7431206, -1.8711254], [52.7431304, -1.8714553], [52.7433397, -1.87189], [52.7434908, -1.8724477], [52.7435809, -1.8731382], [52.7435473, -1.8737017], [52.743528, -1.8739965], [52.7436559, -1.8760682], [52.7435563, -1.8761479], [52.7429855, -1.874488], [52.7417253, -1.8711652], [52.7409824, -1.869593], [52.7401914, -1.867957], [52.7399106, -1.8674558], [52.7396902, -1.8670028], [52.7393423, -1.8664469], [52.7392321, -1.8662678], [52.7392706, -1.8662155], [52.7391113, -1.8658993], [52.7388193, -1.865416], [52.7384565, -1.8648752], [52.7388343, -1.8646814], [52.7388681, -1.8622699]], "tags": {"source": "Bing", "landuse": "residential"}}, {"count": 4, "distance": 27.69962052030919, "points": [[52.7410366, -1.8730072], [52.7407448, -1.8738857], [52.7407005, -1.8746756], [52.7406746, -1.8751371], [52.7405655, -1.8754654], [52.7409285, -1.8756885], [52.7409374, -1.8761565], [52.7407647, -1.876482], [52.7406615, -1.8766266], [52.7404399, -1.8761645], [52.7400755, -1.8763342], [52.7400598, -1.8762327], [52.739948, -1.8762785], [52.7395852, -1.8768481], [52.7391057, -1.877465], [52.7380772, -1.8756036], [52.7381181, -1.8752225], [52.7380051, -1.8745955], [52.737265, -1.8737263], [52.7369766, -1.8736509], [52.7371641, -1.8728095], [52.7372242, -1.8714481], [52.7374044, -1.8707895], [52.7381672, -1.8709975], [52.7382221, -1.8723261], [52.7383448, -1.8728324], [52.7384173, -1.8729984], [52.7385515, -1.8733054], [52.7390895, -1.8736439], [52.739602, -1.8739039], [52.7396898, -1.8728218], [52.7399387, -1.8726767], [52.7405963, -1.8724208], [52.7405887, -1.8729], [52.7410366, -1.8730072]], "average_distance": 506.4055833925352, "tags": {"source": "Bing", "landuse": "residential"}}], "farmland": [{"count": 1, "distance": 470.5167545322967, "points": [[52.7438446, -1.8778869], [52.7458485, -1.8839734], [52.7456583, -1.8840402], [52.7452423, -1.8839067], [52.7449048, -1.8837025], [52.7446766, -1.8834119], [52.7444079, -1.8829171], [52.7442677, -1.882442], [52.7440585, -1.8812679], [52.7439539, -1.8802351], [52.7438469, -1.8791396], [52.7438018, -1.8786055], [52.7438446, -1.8778869]], "average_distance": 641.549676073806, "tags": {"note": "Setting ponds gone - looks like agricultural use (2013-04)", "landuse": "farmland"}}], "industrial": [{"distance": 740.0476325708006, "points": [[52.7454084, -1.8707204], [52.7456557, -1.8698414], [52.745713, -1.8694771], [52.745375, -1.8689634], [52.7440205, -1.8688574], [52.7438851, -1.8691307], [52.7437945, -1.8693657], [52.7437352, -1.8696105], [52.7437822, -1.8697683], [52.7437807, -1.8697949], [52.7437787, -1.8698292], [52.7437238, -1.8699566], [52.7437659, -1.8703704], [52.7454084, -1.8707204]], "tags": {"name": "sewage works", "area": "yes", "man_made": "wastewater_plant", "source": "survey, Bing", "operator": "Severn Trent", "landuse": "industrial"}}, {"count": 2, "distance": 372.82023892264147, "points": [[52.7431131, -1.8853427], [52.7445717, -1.886173], [52.7445532, -1.8870477], [52.745027, -1.8870631], [52.7451609, -1.8843988], [52.7449536, -1.8843461], [52.7446461, -1.8840474], [52.7441444, -1.8829884], [52.7439818, -1.8823131], [52.7437645, -1.8805047], [52.7437031, -1.8798118], [52.7436598, -1.8788557], [52.7436297, -1.8776063], [52.7436658, -1.8772149], [52.743544, -1.8768625], [52.7433112, -1.8775773], [52.743027, -1.8783538], [52.7427256, -1.8788207], [52.7424221, -1.8797131], [52.7426581, -1.8799327], [52.7423736, -1.8810767], [52.7422711, -1.8817356], [52.74211, -1.8828106], [52.7422591, -1.8828375], [52.7424133, -1.8839171], [52.7428062, -1.8836744], [52.7428126, -1.8837091], [52.7431131, -1.8853427]], "average_distance": 616.6908102208133, "tags": {"website": "http://www.ideal-standard.co.uk/", "source:name": "survey", "name": "Ideal Standard", "wikipedia": "en:Armitage Shanks", "man_made": "works", "website2": "http://www.armitage-shanks.co.uk/", "source": "Bing", "old_name": "Armitage Shanks", "landuse": "industrial"}}], "recreation_ground": [{"count": 1, "distance": 168.470009322388, "points": [[52.7415454, -1.8722085], [52.7415104, -1.8716057], [52.7412258, -1.8708778], [52.740872, -1.8712077], [52.7405938, -1.871383], [52.7400338, -1.8712137], [52.7391701, -1.8709296], [52.7387528, -1.8707724], [52.7383026, -1.8703734], [52.7381489, -1.8705548], [52.7381672, -1.8709975], [52.7382221, -1.8723261], [52.7383448, -1.8728324], [52.7384173, -1.8729984], [52.7385515, -1.8733054], [52.7390895, -1.8736439], [52.739602, -1.8739039], [52.7396898, -1.8728218], [52.7399387, -1.8726767], [52.7405963, -1.8724208], [52.7405887, -1.8729], [52.7410366, -1.8730072], [52.7411976, -1.8723628], [52.7415454, -1.8722085]], "average_distance": 320.96938011598996, "tags": {"source": "Bing, OS_OSV", "landuse": "recreation_ground"}}], "farmyard": [{"count": 1, "distance": 546.6804046371739, "points": [[52.7446968, -1.8759421], [52.7445864, -1.875366], [52.7447022, -1.8749033], [52.7447238, -1.8744763], [52.7448221, -1.8743006], [52.7451223, -1.8741515], [52.745156, -1.8745986], [52.7453095, -1.8745942], [52.745296, -1.8748655], [52.7452314, -1.8749211], [52.7453459, -1.8754728], [52.7446968, -1.8759421]], "average_distance": 594.4704184837186, "tags": {"source": "Bing", "landuse": "farmyard", "name": "Old Road Farm"}}]}, "leisure": {"playground": [{"count": 1, "distance": 86.68430240345359, "points": [[52.7402703, -1.8773715], [52.7401099, -1.8775053], [52.7401626, -1.8776779], [52.7403363, -1.8775817], [52.7402703, -1.8773715]], "average_distance": 94.54752806603702, "tags": {"source": "Bing", "leisure": "playground"}}], "social_club": [{"count": 1, "distance": 319.5478306743348, "points": [[52.74173, -1.8802163], [52.7417269, -1.8799578], [52.7416507, -1.8799603], [52.7416511, -1.8799928], [52.7416018, -1.8799944], [52.7416021, -1.8800174], [52.7415699, -1.8800185], [52.7415721, -1.8802], [52.7416141, -1.8801987], [52.7416144, -1.8802201], [52.74173, -1.8802163]], "average_distance": 328.5053134701109, "tags": {"building": "yes", "source": "Bing;survey", "name": "Armitage Royal British Legion", "leisure": "social_club"}}], "park": [{"count": 4, "distance": 467.7541644444348, "points": [[52.7416924, -1.8702717], [52.7419244, -1.8702913], [52.7421181, -1.8703588], [52.7422314, -1.8703718], [52.7422921, -1.8701541], [52.7422394, -1.8697275], [52.7420773, -1.8688719], [52.7420443, -1.8685758], [52.7420364, -1.868282], [52.7421194, -1.8679641], [52.7419824, -1.8682742], [52.7417741, -1.8687456], [52.7416581, -1.8690722], [52.7416173, -1.8693552], [52.7416199, -1.8698341], [52.7416397, -1.8702195], [52.7416924, -1.8702717]], "average_distance": 569.6849070969648, "tags": {"source": "Bing", "landuse": "grass", "leisure": "park"}}, {"distance": 610.1018117771575, "points": [[52.7432471, -1.8694717], [52.7432155, -1.8695533], [52.742736, -1.8695962], [52.7427224, -1.8692154], [52.7427873, -1.869151], [52.7428523, -1.8689954], [52.7428942, -1.8689902], [52.7430244, -1.868974], [52.7431348, -1.8689418], [52.74319, -1.8692532], [52.7432471, -1.8694717]], "tags": {"source": "Bing", "landuse": "grass", "leisure": "park"}}, {"distance": 627.669602753853, "points": [[52.7402738, -1.8671231], [52.7401988, -1.8670664], [52.740161, -1.8670177], [52.740161, -1.8669306], [52.7401988, -1.8668116], [52.7402374, -1.8667444], [52.7402738, -1.8671231]], "tags": {"leisure": "park"}}, {"distance": 610.1018117771575, "points": [[52.7432471, -1.8694717], [52.7433524, -1.8693709], [52.7432777, -1.8708142], [52.7433849, -1.8718227], [52.7434596, -1.8722143], [52.7433362, -1.8718547], [52.743177, -1.8714955], [52.7431413, -1.8714255], [52.7431409, -1.8713183], [52.7431495, -1.8708918], [52.7430886, -1.8706396], [52.7427771, -1.8706396], [52.742736, -1.8695962], [52.74285, -1.8689847], [52.7431336, -1.868936], [52.7432375, -1.8694042], [52.7432428, -1.8694417], [52.7432471, -1.8694717]], "tags": {"source": "Bing", "landuse": "grass", "leisure": "park"}}], "common": [{"count": 3, "distance": 85.2429871455547, "points": [[52.7395372, -1.8741869], [52.7393967, -1.8748247], [52.7392671, -1.8753665], [52.7391522, -1.8752571], [52.7390711, -1.8751388], [52.7390017, -1.8749091], [52.7389732, -1.8748242], [52.7389076, -1.8747594], [52.738991, -1.8743391], [52.7390738, -1.8738309], [52.7392285, -1.8738907], [52.739336, -1.8739561], [52.7395372, -1.8741869]], "average_distance": 410.73179097651416, "tags": {"leisure": "common"}}, {"distance": 539.9390089013301, "points": [[52.7385654, -1.8686058], [52.7385838, -1.8687973], [52.7387298, -1.8687579], [52.7387348, -1.867864], [52.7382911, -1.8678446], [52.7382501, -1.8686152], [52.7385654, -1.8686058]], "tags": {"leisure": "common"}}, {"distance": 534.6099773366211, "points": [[52.7381453, -1.8688913], [52.7379715, -1.8688779], [52.7379666, -1.8684326], [52.737978, -1.8680625], [52.7380153, -1.8676816], [52.738077, -1.8673678], [52.7381923, -1.8674295], [52.7380868, -1.8676467], [52.7380641, -1.8678023], [52.7380917, -1.8679686], [52.7381095, -1.8682341], [52.7380949, -1.8684943], [52.7381063, -1.8686338], [52.7381436, -1.8687464], [52.7381453, -1.8688913]], "tags": {"leisure": "common"}}], "pitch": [{"distance": 269.74066979204605, "points": [[52.7389023, -1.8726219], [52.7389416, -1.8721595], [52.738575, -1.8720744], [52.7385357, -1.8725369], [52.7389023, -1.8726219]], "tags": {"source": "Bing", "sport": "soccer", "leisure": "pitch"}}, {"distance": 232.47374151582568, "points": [[52.739443, -1.8729751], [52.7395209, -1.8724547], [52.7392124, -1.8723421], [52.7391409, -1.872857], [52.739443, -1.8729751]], "tags": {"source": "Bing", "sport": "multi", "leisure": "pitch", "barrier": "fence"}}, {"count": 4, "distance": 30.788447807615565, "points": [[52.7401932, -1.8771873], [52.7399471, -1.8766362], [52.7392618, -1.8774709], [52.7395079, -1.878022], [52.7401932, -1.8771873]], "average_distance": 233.41774543112746, "tags": {"source": "Bing", "sport": "soccer", "leisure": "pitch"}}, {"distance": 315.6212362972576, "points": [[52.7386462, -1.8720535], [52.7394941, -1.8723276], [52.7395769, -1.8716289], [52.738729, -1.8713547], [52.7386462, -1.8720535]], "tags": {"source": "Bing", "sport": "soccer", "leisure": "pitch"}}]}}, "closest_pois": {"amenity": {"place_of_worship": {"count": 1, "distance": 562.3483373205014, "points": [[52.7416633, -1.8683293], [52.7416791, -1.8686422], [52.7416015, -1.8686529], [52.7415857, -1.86834], [52.7416633, -1.8683293]], "average_distance": 576.039636148863, "tags": {"religion": "christian", "amenity": "place_of_worship", "name": "Handsacre Methodist Church", "denomination": "methodist"}}, "school": {"count": 2, "distance": 748.2482614300812, "points": [[52.7432761, -1.8866251], [52.743402, -1.8861864], [52.7435586, -1.886309], [52.743609, -1.886133], [52.7434833, -1.8860346], [52.7435744, -1.8857168], [52.743461, -1.885628], [52.7431935, -1.8865604], [52.7432761, -1.8866251]], "average_distance": 831.7944365701372, "tags": {"building": "school", "amenity": "school", "name": "Croft Primary School", "addr:street": "Rugeley Road"}}, "post_box": {"count": 2, "distance": 244.00876409375252, "points": [[52.7418357, -1.8755]], "average_distance": 483.41690800426056, "tags": {"amenity": "post_box", "ref": "WS15 312"}}, "veterinary": {"count": 1, "distance": 307.257307212886, "points": [[52.7419633, -1.8790418]], "average_distance": 307.257307212886, "tags": {"amenity": "veterinary", "name": "Pool House Veterinary Clinic"}}, "pub": {"count": 2, "distance": 453.3890140640647, "points": [[52.7418357, -1.8821472]], "average_distance": 629.3970417063672, "tags": {"amenity": "pub", "name": "The Swan Inn"}}, "parking": {"count": 4, "distance": 183.27311932030563, "points": [[52.7393683, -1.8737368], [52.7394495, -1.8731843], [52.739339, -1.873136], [52.7392871, -1.8734364], [52.7392578, -1.8734418], [52.7392416, -1.8735169], [52.7389006, -1.873372], [52.7388811, -1.8734739], [52.7393683, -1.8737368]], "average_distance": 373.43496447981386, "tags": {"amenity": "parking"}}, "post_office": {"count": 1, "distance": 249.9964286650557, "points": [[52.7419064, -1.8756069]], "average_distance": 249.9964286650557, "tags": {"source": "survey", "amenity": "post_office"}}}, "landuse": {"industrial": {"count": 2, "distance": 372.82023892264147, "points": [[52.7431131, -1.8853427], [52.7445717, -1.886173], [52.7445532, -1.8870477], [52.745027, -1.8870631], [52.7451609, -1.8843988], [52.7449536, -1.8843461], [52.7446461, -1.8840474], [52.7441444, -1.8829884], [52.7439818, -1.8823131], [52.7437645, -1.8805047], [52.7437031, -1.8798118], [52.7436598, -1.8788557], [52.7436297, -1.8776063], [52.7436658, -1.8772149], [52.743544, -1.8768625], [52.7433112, -1.8775773], [52.743027, -1.8783538], [52.7427256, -1.8788207], [52.7424221, -1.8797131], [52.7426581, -1.8799327], [52.7423736, -1.8810767], [52.7422711, -1.8817356], [52.74211, -1.8828106], [52.7422591, -1.8828375], [52.7424133, -1.8839171], [52.7428062, -1.8836744], [52.7428126, -1.8837091], [52.7431131, -1.8853427]], "average_distance": 616.6908102208133, "tags": {"website": "http://www.ideal-standard.co.uk/", "source:name": "survey", "name": "Ideal Standard", "wikipedia": "en:Armitage Shanks", "man_made": "works", "website2": "http://www.armitage-shanks.co.uk/", "source": "Bing", "old_name": "Armitage Shanks", "landuse": "industrial"}}, "reservoir": {"count": 3, "distance": 696.2703283781167, "points": [[52.7445355, -1.8689845], [52.7445227, -1.8694229], [52.7444809, -1.8694853], [52.7443613, -1.8694754], [52.7444609, -1.8689766], [52.7445355, -1.8689845]], "average_distance": 750.6871155510211, "tags": {"source": "Bing", "landuse": "reservoir"}}, "orchard": {"count": 1, "distance": 516.4200986407017, "points": [[52.742736, -1.8695962], [52.7427771, -1.8706396], [52.7430886, -1.8706396], [52.7431071, -1.8704424], [52.7431776, -1.8702959], [52.7432367, -1.8700781], [52.7432155, -1.8695533], [52.742736, -1.8695962]], "average_distance": 561.224063429874, "tags": {"landuse": "orchard"}}, "residential": {"count": 4, "distance": 27.69962052030919, "points": [[52.7410366, -1.8730072], [52.7407448, -1.8738857], [52.7407005, -1.8746756], [52.7406746, -1.8751371], [52.7405655, -1.8754654], [52.7409285, -1.8756885], [52.7409374, -1.8761565], [52.7407647, -1.876482], [52.7406615, -1.8766266], [52.7404399, -1.8761645], [52.7400755, -1.8763342], [52.7400598, -1.8762327], [52.739948, -1.8762785], [52.7395852, -1.8768481], [52.7391057, -1.877465], [52.7380772, -1.8756036], [52.7381181, -1.8752225], [52.7380051, -1.8745955], [52.737265, -1.8737263], [52.7369766, -1.8736509], [52.7371641, -1.8728095], [52.7372242, -1.8714481], [52.7374044, -1.8707895], [52.7381672, -1.8709975], [52.7382221, -1.8723261], [52.7383448, -1.8728324], [52.7384173, -1.8729984], [52.7385515, -1.8733054], [52.7390895, -1.8736439], [52.739602, -1.8739039], [52.7396898, -1.8728218], [52.7399387, -1.8726767], [52.7405963, -1.8724208], [52.7405887, -1.8729], [52.7410366, -1.8730072]], "average_distance": 506.4055833925352, "tags": {"source": "Bing", "landuse": "residential"}}, "recreation_ground": {"count": 1, "distance": 168.470009322388, "points": [[52.7415454, -1.8722085], [52.7415104, -1.8716057], [52.7412258, -1.8708778], [52.740872, -1.8712077], [52.7405938, -1.871383], [52.7400338, -1.8712137], [52.7391701, -1.8709296], [52.7387528, -1.8707724], [52.7383026, -1.8703734], [52.7381489, -1.8705548], [52.7381672, -1.8709975], [52.7382221, -1.8723261], [52.7383448, -1.8728324], [52.7384173, -1.8729984], [52.7385515, -1.8733054], [52.7390895, -1.8736439], [52.739602, -1.8739039], [52.7396898, -1.8728218], [52.7399387, -1.8726767], [52.7405963, -1.8724208], [52.7405887, -1.8729], [52.7410366, -1.8730072], [52.7411976, -1.8723628], [52.7415454, -1.8722085]], "average_distance": 320.96938011598996, "tags": {"source": "Bing, OS_OSV", "landuse": "recreation_ground"}}, "farmland": {"count": 1, "distance": 470.5167545322967, "points": [[52.7438446, -1.8778869], [52.7458485, -1.8839734], [52.7456583, -1.8840402], [52.7452423, -1.8839067], [52.7449048, -1.8837025], [52.7446766, -1.8834119], [52.7444079, -1.8829171], [52.7442677, -1.882442], [52.7440585, -1.8812679], [52.7439539, -1.8802351], [52.7438469, -1.8791396], [52.7438018, -1.8786055], [52.7438446, -1.8778869]], "average_distance": 641.549676073806, "tags": {"note": "Setting ponds gone - looks like agricultural use (2013-04)", "landuse": "farmland"}}, "grass": {"count": 5, "distance": 27.69962052030919, "points": [[52.7406615, -1.8766266], [52.7405176, -1.876956], [52.7404051, -1.8768619], [52.7403669, -1.8768495], [52.7402552, -1.877003], [52.7403864, -1.877356], [52.7405578, -1.8777592], [52.7404865, -1.8778343], [52.7401716, -1.8781197], [52.7401482, -1.8780794], [52.7400465, -1.8782108], [52.7398821, -1.8780572], [52.7394969, -1.8783117], [52.7391057, -1.877465], [52.7395852, -1.8768481], [52.739948, -1.8762785], [52.7400598, -1.8762327], [52.7400755, -1.8763342], [52.7404399, -1.8761645], [52.7406615, -1.8766266]], "average_distance": 440.2782360378488, "tags": {"landuse": "grass"}}, "farmyard": {"count": 1, "distance": 546.6804046371739, "points": [[52.7446968, -1.8759421], [52.7445864, -1.875366], [52.7447022, -1.8749033], [52.7447238, -1.8744763], [52.7448221, -1.8743006], [52.7451223, -1.8741515], [52.745156, -1.8745986], [52.7453095, -1.8745942], [52.745296, -1.8748655], [52.7452314, -1.8749211], [52.7453459, -1.8754728], [52.7446968, -1.8759421]], "average_distance": 594.4704184837186, "tags": {"source": "Bing", "landuse": "farmyard", "name": "Old Road Farm"}}}, "leisure": {"pitch": {"count": 4, "distance": 30.788447807615565, "points": [[52.7401932, -1.8771873], [52.7399471, -1.8766362], [52.7392618, -1.8774709], [52.7395079, -1.878022], [52.7401932, -1.8771873]], "average_distance": 233.41774543112746, "tags": {"source": "Bing", "sport": "soccer", "leisure": "pitch"}}, "social_club": {"count": 1, "distance": 319.5478306743348, "points": [[52.74173, -1.8802163], [52.7417269, -1.8799578], [52.7416507, -1.8799603], [52.7416511, -1.8799928], [52.7416018, -1.8799944], [52.7416021, -1.8800174], [52.7415699, -1.8800185], [52.7415721, -1.8802], [52.7416141, -1.8801987], [52.7416144, -1.8802201], [52.74173, -1.8802163]], "average_distance": 328.5053134701109, "tags": {"building": "yes", "source": "Bing;survey", "name": "Armitage Royal British Legion", "leisure": "social_club"}}, "park": {"count": 4, "distance": 467.7541644444348, "points": [[52.7416924, -1.8702717], [52.7419244, -1.8702913], [52.7421181, -1.8703588], [52.7422314, -1.8703718], [52.7422921, -1.8701541], [52.7422394, -1.8697275], [52.7420773, -1.8688719], [52.7420443, -1.8685758], [52.7420364, -1.868282], [52.7421194, -1.8679641], [52.7419824, -1.8682742], [52.7417741, -1.8687456], [52.7416581, -1.8690722], [52.7416173, -1.8693552], [52.7416199, -1.8698341], [52.7416397, -1.8702195], [52.7416924, -1.8702717]], "average_distance": 569.6849070969648, "tags": {"source": "Bing", "landuse": "grass", "leisure": "park"}}, "playground": {"count": 1, "distance": 86.68430240345359, "points": [[52.7402703, -1.8773715], [52.7401099, -1.8775053], [52.7401626, -1.8776779], [52.7403363, -1.8775817], [52.7402703, -1.8773715]], "average_distance": 94.54752806603702, "tags": {"source": "Bing", "leisure": "playground"}}, "common": {"count": 3, "distance": 85.2429871455547, "points": [[52.7395372, -1.8741869], [52.7393967, -1.8748247], [52.7392671, -1.8753665], [52.7391522, -1.8752571], [52.7390711, -1.8751388], [52.7390017, -1.8749091], [52.7389732, -1.8748242], [52.7389076, -1.8747594], [52.738991, -1.8743391], [52.7390738, -1.8738309], [52.7392285, -1.8738907], [52.739336, -1.8739561], [52.7395372, -1.8741869]], "average_distance": 410.73179097651416, "tags": {"leisure": "common"}}}}}

road_data = {"roads":
                 {"points": [[53.7395813, -1.8762029], [51.7394521, -1.8764498]],
                  "segment": {"distance": 4.2195456666296162e-08, "points": [[53.7395813, -1.8762029], [51.7394521, -1.8764498]],
                              "segment-point": [52.739527997684355, -1.8763047602301295]},
                  "tags": {"source": "Bing, OS_Locator", "name": "Wordsworth Close", "highway": "residential"}}
             }

from geopy.distance import vincenty
import time


def calculateDistance(p1, p2):
    # print "Reversed", p1, p2
    distance = vincenty(reversed(p1), reversed(p2)).meters
    #print p1[::-1], p2[::-1], distance
    return distance

def calculateSegmentLengths(segments):
    result = 0
    s1 = segments[0]
    #for segment in segments:
    for i in range(1, len(segments)):
        s2 = segments[i]
        result += calculateDistance(s1, s2)
        s1 = s2
    return result

def calculateLength(points):
    if len(points) <= 1:
        return 0
    result = 0
    p1 = points[0]
    for i in range(1, len(points)):
        p2 = points[i]
        result += calculateDistance(p1, p2)
        p1 = p2
    return result

def cutoffPoints(left_cutoff, points):
    #if len(points) > 3:
    if left_cutoff:
        return points[1:]
    else:
        return points[:-1]
    #else:
    #    return points

def calculateCloserPoint(p1, p2, percentage):
    print p1, p2, percentage
    pointx = p1[0] + (p2[0] - p1[0]) * percentage
    pointy = p1[1] + (p2[1] - p1[1]) * percentage
    result = [pointx, pointy]
    return result

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def shortenSegment(points, middle_point, length_over, length_left, length_right, max_length):
    print "Lengths", length_left, length_right, (length_left == length_right), isclose(length_left, length_right)
    # if length_left == length_right:
    if isclose(length_left, length_right):
        # shorten both with length_over / 2
        point_left = calculateCloserPoint(middle_point, points[0], ((max_length/2)) / length_left)
        point_right = calculateCloserPoint(middle_point, points[1], ((max_length/2)) / length_right)
        print "Cutting both", [point_left, point_right]
        return [point_left, point_right]
    elif length_left > length_right:
        # shorten left with length_left - length_right
        noemer = length_right
        if length_right > length_left:
            noemer = (max_length - length_right)
        point_left = calculateCloserPoint(middle_point, points[0], noemer / length_left)
        print "Cutting left", [point_left, points[1]]
        return [point_left, points[1]]
    else: #  length_left < length_right:
        # shorten_right with length_right - length_left
        noemer = length_left
        if length_left > length_right:
            noemer = (max_length - length_left)
        point_right = calculateCloserPoint(middle_point, points[1], noemer / length_right)
        print "Cutting right", [points[0], point_right]
        return [points[0], point_right]

def minimizeLength(location, road_data, max_length):
    points = road_data['roads']['points']
    segment_part = road_data['roads']['segment']['points']
    segment_point = road_data['roads']['segment']['segment-point']

    print "STARTING", points, segment_part, segment_point

    current_length = calculateLength(points)
    while current_length > max_length:

        over_middle = False
        left = []
        right = []
        point1 = points[0]
        i = 1

        if len(points) < 3:
            left = [points[0], segment_point]
            right = [segment_point, points[1]]
        else:
            while i < len(points):
                point2 = points[i]
                current_segment = [point1, point2]
                if not over_middle:
                    if current_segment != segment_part:
                        print "Left ", current_segment
                        left.append(current_segment)
                    else:
                        print "Left ", [point1, segment_point]
                        left.append([point1, segment_point])
                        print "Right ", [segment_point, point2]
                        right.append([segment_point, point2])
                        over_middle = True
                else:
                    print "Right ", current_segment
                    right.append(current_segment)
                point1 = point2
                i += 1

        print "Segments", left, right
        length_left = calculateSegmentLengths(left)
        length_right = calculateSegmentLengths(right)

        print "Lengths", length_left, length_right, current_length

        length_over = max_length - current_length
        if len(points) > 3:
            points = cutoffPoints(True, points)
        else:
            points = shortenSegment(points, segment_point, length_over, length_left, length_right, max_length)
        print "New points", points
        current_length = calculateLength(points)

        print "New length", current_length


        #time.sleep(100)

        # cut-off

        #current_length = calculateLength(points)
    time.sleep(2)
    return points

points = road_data['roads']['points']
location = [52.73971, -1.8764]
print len(points)
print calculateLength(points)
points = minimizeLength(location, road_data, 200.0)
print len(points)
print calculateLength(points)
