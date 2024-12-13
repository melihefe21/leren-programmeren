<?php

namespace App\Http\Controllers;

use App\Models\Song;
use Illuminate\Http\Request;

class ViewsController extends Controller
{
    public function index()
    {
        // Fetch songs with their associated genre
        $songs = Song::with('genre')->get();

        // Pass the data to the view
        return view('views.index', compact('songs'));
    }
}
