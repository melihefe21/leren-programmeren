<?php
namespace Database\Seeders;
use Illuminate\Support\Facades\DB;
use Illuminate\Database\Seeder;
use App\Models\Song;
use App\Models\Genre;

class SongSeeder extends Seeder
{
    public function run()
    {
        $genre = Genre::firstOrCreate(['name' => 'Pop']);

        $songs = [
            ['name' => 'Bohemian Rhapsody', 'artist' => 'Queen', 'duration' => 354, 'genre_id' => $genre->id],
            ['name' => 'Hotel California', 'artist' => 'Eagles', 'duration' => 391, 'genre_id' => $genre->id],
            ['name' => 'Stairway to Heaven', 'artist' => 'Led Zeppelin', 'duration' => 482, 'genre_id' => $genre->id],
            ['name' => 'Imagine', 'artist' => 'John Lennon', 'duration' => 183, 'genre_id' => $genre->id],
            ['name' => 'Hey Jude', 'artist' => 'The Beatles', 'duration' => 431, 'genre_id' => $genre->id],
        ];

        foreach ($songs as $song) {
            Song::create($song);
        }
    }
}


