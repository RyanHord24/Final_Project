
export default function MapComponent() {
    var map = L.map('map', {
        center: [51.505, -0.09],
        zoom: 13
    });
    return map
}