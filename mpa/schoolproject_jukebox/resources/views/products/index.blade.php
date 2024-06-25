@extends("layout.master")

@section("content")
    <h1>dit is de content van mijn begroetingspagina</h1>
    <ul>
        @foreach ($handmade as $made)
        <li>{{$made->name}} -{{}} </li>
        @endforeach
        {{$handmade}}
    </ul>    
    <ul>
        <li>

        </li>
    </ul>
    @endsection

    @push("js")
    <script>
        alert 'je dikke kkr moeder'
    </script>
    @endpush