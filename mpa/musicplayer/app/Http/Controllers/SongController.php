<?php

namespace App\Http\Controllers;

use App\Models\Song;
use Illuminate\Http\Request;

class SongController extends Controller
{
    public function index()
    {
        $songs = Song::with('genre')->get();
        return view('songs.index', compact('songs'));
    }

    public function about()
    {
        return view('songs.about');
    }
}
