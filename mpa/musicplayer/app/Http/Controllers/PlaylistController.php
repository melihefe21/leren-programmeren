<?php

namespace App\Http\Controllers;
use App\Models\Song;
use App\Models\Playlist;
use Illuminate\Http\Request;

class PlaylistController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $playlists = PLaylist::all();
        return view("playlist.index", ["playlists" => $playlists]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Playlist $playlist)
    {
        $songs = Song::all();
        return view("playlists.show", ["playlists"=> $playlist, "songs"=> $songs]);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Playlist $playlist)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Playlist $playlist)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Playlist $playlist)
    {
        //
    }

    public function AddSongtoPlaylist(request $request,Playlist $playlist){
        $song = $request->get("selectedsong");
        dd($song);
        $playlist->songs()->attach($song);
        return redirect()->back();
    }
}
