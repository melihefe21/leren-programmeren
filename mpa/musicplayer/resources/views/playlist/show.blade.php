@extends("layouts.master")


@section("content")
    <h1>{{$playlist->name}}</h1>
    <p>{{$playlist->description}}</p>
    @foreach ($playlist->songs as $song)
     -{{$song->name}}

     @foreach($playlists as $playlist)
    <p>{{$playlist->name}}</p> - 
    @endforeach
    @foreach ($playlist->songs as $song) -{{$song->name}}

    @endforeach

    <form action="/playlist/addsong/{{$playlist->id}}" method="POST">
        @csrf
        <input type="submit" value="Send me!">

        <select name="selectedsong">
            @foreach(songs as $song)
                <option value="{{$song->id}}">{{$song->name}}</option>
            $endforeach
        </select>
    </form>

@endsection