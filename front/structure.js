// GET /api/album (liste d'objets)
const albums = [
    {
        id: 1,
        name: "Homework1",
        author: "Daft Punk", // Peut être un objet (à définir)
        price: 25.00,
        category: "House music",
        songs: [
            {
                id: 1,
                name: "Daftendirekt",
                time: "2:45"
            },
            {
                id: 2,
                name: "WDPK 83.7 FM",
                time: "28"
            },
            {
                id: 3,
                name: "Revolution 909",
                time: "5:35"
            },
            {
                id: 4,
                name: "Da funk",
                time: "3:29"
            },
        ]
    },
    {
        id: 2,
        name: "Homework2",
        author: "Daft Punk", // Peut être un objet (à définir)
        price: 25.00,
        category: "House music",
        songs: [
            {
                id: 5,
                name: "Daftendirekt2",
                time: "2:45"
            },
            {
                id: 6,
                name: "WDPK 83.7 FM2",
                time: "28"
            },
            {
                id: 7,
                name: "Revolution 9092",
                time: "5:35"
            },
            {
                id: 8,
                name: "Da funk2",
                time: "3:29"
            },
        ]
    },
]
// GET /api/album/{id} (objet)
// Résultat de /api/album/1
const album = {
    id: 1,
    name: "Homework1",
    author: "Daft Punk", // Peut être un objet (à définir)
    price: 25.00,
    category: "House music",
    songs: [
        {
            id: 1,
            name: "Daftendirekt",
            time: "2:45"
        },
        {
            id: 2,
            name: "WDPK 83.7 FM",
            time: "28"
        },
        {
            id: 3,
            name: "Revolution 909",
            time: "5:35"
        },
        {
            id: 4,
            name: "Da funk",
            time: "3:29"
        },
    ]
}
// GET /api/album/song (liste d'objets)
// Résultat de /api/album/song
const songs = [
    {
        id: 1,
        name: "Daftendirekt",
        time: "2:45"
    },
    {
        id: 2,
        name: "WDPK 83.7 FM",
        time: "28"
    },
    {
        id: 3,
        name: "Revolution 909",
        time: "5:35"
    },
    {
        id: 4,
        name: "Da funk",
        time: "3:29"
    },
]


// GET /api/cart/{email}
// POST /api/cart/{email}
const cart = {
    id: 1,
    email: 'legrandt84@gmail.com',
    products: [
        {
            id: 1,
            quantity: 2,
        },
        {
            id: 2,
            quantity: 1,
        },
        {
            id: 3,
            quantity: 2,
        },
    ]
}

// POST /api/order (envoie un objet) y rajouter une datetime (createAt)
const orders = [
    {
        id: 1,
        total: 125.00,
        products: [
            {
                id: 1,
                quantity: 2,
            },
            {
                id: 2,
                quantity: 1,
            },
            {
                id: 3,
                quantity: 2,
            },
        ]
    }
]
