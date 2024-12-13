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

        Song::create([
            'name' => 'Example liedj',
            'genre_id' => $genre->id,
        ]);
    }
}

{
    {
        DB::table('songs')->insert([
            ['title' => 'Bohemian Rhapsody', 'artist' => 'Queen'],
            ['title' => 'Hotel California', 'artist' => 'Eagles'],
            ['title' => 'Stairway to Heaven', 'artist' => 'Led Zeppelin'],
            ['title' => 'Imagine', 'artist' => 'John Lennon'],
            ['title' => 'Hey Jude', 'artist' => 'The Beatles'],
        ]);
    }
}



